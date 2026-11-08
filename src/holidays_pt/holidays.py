import calendar
from datetime import datetime, timedelta
from functools import wraps
from typing import Any

from holidays_pt._easter import calculate_easter
from holidays_pt.codes import select as select_codes
from holidays_pt.exceptions import MissingColumnError, NoBankHolidaysError
from holidays_pt.models import Year
from holidays_pt.regions import select as select_regions

# define a calendar with the first day of the week as monday to calculate
# moving holidays
CLD = calendar.Calendar(firstweekday=calendar.MONDAY)


def _convert_codes(year: int, check: str, keys: list[int]) -> datetime:
    """Calculate the holiday for a given year.

    Parameters
    ----------
    year : int
        year of the holiday
    check : {'f', 'e', 'm', 's'}
        type of holiday
    codes : list[int]
        list wtih values used to calculate the holiday date

    Returns
    -------
    date: datetime
        date of the holiday in the given year

    Notes
    -----
    For moving holidays which usually are stated like "the second sunday of the
    given month", the method for caculating is as follow:
    - generate a list of weeks for the given month and year (calendar.monthdatescalendar);
    - select the week (by list slicing);
    - select the day (the week starts on a monday);
    """

    if check == "f":  # fix days
        return datetime(year, keys[0], keys[1])
    elif check == "e":  # holidays calculated based on easter day
        return calculate_easter(Year(year)) + timedelta(days=keys[0])
    elif check == "m":  # moving holidays
        holi = CLD.monthdatescalendar(year, keys[0])[keys[1]][keys[2]]
        # TODO: remove this after checkup
        # return to_datetime(CLD.monthdatescalendar(year, keys[0])[keys[1]][keys[2]])
        return datetime(holi.year, holi.month, holi.day)
    elif check == "s":  # special case from 'lousada'
        return datetime(
            year, 7, max(w[-1] for w in calendar.monthcalendar(year, 7))
        ) + timedelta(days=1)
    else:
        return None


def _calc_holiday_date(
    years: list[int], holidays: dict[str, str | list[int]]
) -> dict[str, str | datetime]:
    """convert codes to date for the given years"""
    new_dicts = []
    for year in years:
        for h in holidays:
            tmp_dict = h.copy()
            [tmp_dict.pop(x, None) for x in ["type", "codes"]]
            tmp_dict["date"] = _convert_codes(year, h["type"], h["codes"])
            new_dicts.append(tmp_dict)
    return new_dicts


def check_holidays(method):
    """Check if the object in Holidays has any holidays calculated."""

    @wraps(method)
    def wrapper(*args, **kwargs):
        if args[0].holidays is None:
            raise NoBankHolidaysError
        else:
            return method(*args, **kwargs)

    return wrapper


class Holidays:
    """Class to generate the holidays dates for a period of time.

    Examples
    --------
    >>> from holidays import Holidays
    >>> hol = holidays.Holidays('2021-01-01', '2021-12-31')
    >>> hol.calculate()
    Holidays(start_date=2021-01-01, end_date=2021-12-31)
    >>> hol.as_list()
    """

    def __init__(
        self, start_date: str, end_date: str, date_format: str = "%Y-%m-%d"
    ) -> None:
        """Define date period to calculate the holidays.

        Parameters
        ----------
        start_date : str, '%Y-%m-%d' (ex: 2020-05-15)
            start of the period in the format
        end_date : str, '%Y-%m-%d' (ex: 2020-05-15)
            end of the period
        date_format : str, default='%Y-%m-%d'
            string describing th date format used
        """

        self.start_date = start_date
        self.end_date = end_date
        self._date_format = date_format

        self._start_date: datetime = datetime.strptime(start_date, self._date_format)
        self._end_date: datetime = datetime.strptime(end_date, self._date_format)

        self.years: set[int] = set(
            [self._start_date.year]
            + list(range(self._start_date.year, self._end_date.year + 1))
        )

        self.holidays: Any | None = None

    def __repr__(self) -> str:
        return f"Holidays(start_date={self.start_date}, end_date={self.end_date})"

    def __contains__(self, item: str) -> bool:
        """Check whether a date is between the given range."""
        return (
            self._start_date
            <= datetime.strptime(item, self._date_format)
            <= self._end_date
        )

    @check_holidays
    def __len__(self) -> int:
        """Return count of holidays in the date range."""
        return int(self.holidays.shape[0])

    def leap_years(self) -> dict[int, bool]:
        """Check if years are leap years or not."""
        return {i: calendar.isleap(i) for i in self.years}

    def calculate(
        self,
        district: list[str] | None = None,
        county: list[str] | None = None,
        extent: str | None = "national",
    ) -> "Holidays":
        """Calculate the holidays for the select time period"""

        _holidays = []
        if district or county:
            selected_regions = select_regions(district=district, county=county)
            _holidays += select_codes(codes=selected_regions)

        if extent:
            _holidays += select_codes(codes=extent)

        # remove dupes
        _holidays = [i for n, i in enumerate(_holidays) if i not in _holidays[n + 1 :]]
        _holidays = _calc_holiday_date(years=self.years, holidays=_holidays)

        self.holidays = []
        for h in _holidays:
            if self._start_date <= h["date"] <= self._end_date:
                self.holidays.append(h)
        return self

    @check_holidays
    def date_str(self, date_format: str | None = None) -> "Holidays":
        """Convert dates to string format"""

        if date_format is None:
            date_format = self._date_format

        if isinstance(self.holidays[0]["date"], datetime):
            converted_date = []
            for h in self.holidays:
                h["date"] = h["date"].strftime(date_format)
                converted_date.append(h)
            self.holidays = converted_date

        return self

    @check_holidays
    def drop(self, columns: list[str]) -> "Holidays":
        """Remove columns not needed"""

        if not columns:
            raise MissingColumnError("Requires a column to remove")
        if not isinstance(columns, list) and not isinstance(columns, tuple):
            raise MissingColumnError("Requires a iterable with column names")

        existing_cols = self.holidays[0].keys()
        for col in columns:
            if col not in existing_cols:
                raise MissingColumnError("That column does not exists")

        droped_cols = []
        for h in self.holidays:
            tmp_dict = h.copy()
            [tmp_dict.pop(x, None) for x in columns]
            droped_cols.append(tmp_dict)
        self.holidays = droped_cols

        return self

    @check_holidays
    def as_list(self) -> list[dict[str, str | datetime]]:
        """Return a list of dicts with the required information"""
        return self.holidays

    @staticmethod
    def ls(extent: str = "national"):
        """Return table with available national/regional or all holidays"""

        calculated_holidays = _calc_holiday_date(
            years=[datetime.now().year], holidays=select_codes(codes=extent)
        )

        converted_date = []
        for h in calculated_holidays:
            h["date"] = h["date"].strftime("%Y-%m-%d")
            converted_date.append(h)

        return converted_date
