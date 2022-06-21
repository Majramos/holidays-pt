#!/usr/bin/env python
# coding: utf-8

"""
Module to calculate the holidays for a date range
"""

import itertools
import json
from functools import wraps

from datetime import datetime, timedelta
from dateutil.easter import easter
import calendar

from typing import List, Dict, Union, Set, Optional

import pandas as pd


# DECLARE TYPE VARIABLES
ListorStr = Union[str, List[str]]


# weeks days accoding to the iso norm
WEEKDAYS = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',
            5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

# define a calendar with the first day of the week as monday to calculate
# moving holidays
CLD = calendar.Calendar(firstweekday=calendar.MONDAY)


# import data
try:
    with open('holidays.json') as json_file:
        data = json.load(json_file)
except Exception:
    # read file in the package
    import importlib.resources as pkg_resources
    data = json.load(pkg_resources.open_text(__package__, 'holidays.json'))
else:
    pass


HOLIDAYS: pd.DataFrame = pd.DataFrame.from_dict(data['holidays'], orient='index')
__regions = pd.json_normalize(data['regions']).T.reset_index().rename(columns={0: 'holidays'})
__regions_levels = __regions['index'].str.split(pat='.', expand=True)
__regions_levels = __regions_levels.rename(
    columns={i: ('level'+str(i) if i != 0 else 'country') for i in __regions_levels.columns}
)
REGIONS = pd.concat([__regions, __regions_levels], axis=1).drop(columns='index')


def _validate_inputs(inputs, compare):
    """ Check if inputs are valid.
    Convert to list to work with dataframe slicing.
    """
    if inputs in compare or inputs == compare or set(inputs).issubset(set(compare)):
        if isinstance(inputs, list):
            return inputs
        else:  # converto to list if necessary
            return [inputs]
    else:
        raise Exception(f'The input {inputs} is not supported. Please choose from: {compare}')


def _select_regional(country: List[str], *, level1: Optional[List[str]] = None,
                     level2: Optional[List[str]] = None, as_list: bool = True) -> List[str]:
    """ Select all the required regional holidays by location.

    Parameters
    ----------
    country : str, {'PT', 'ES'}
        Country where to calculate the holidays
    nivel1 : str, default=None
        Corresponds to district in Portugal or autonomos region in Spain.
    nivel2 : str, default=None
        Corresponds to a county in Portugal/Spain.
    as_list : bool, default=True
        Select format of the output. To be used internally by Holidays.

    Returns
    -------
    output : list or dataframe
        List or table with the selected holidays
    """

    level1 = REGIONS['level1'].unique() if level1 is None else level1
    level2 = REGIONS['level2'].unique() if level2 is None else level2

    output = REGIONS[REGIONS.country.isin(country) &
                     REGIONS.level1.isin(level1) &
                     REGIONS.level2.isin(level2)]

    if as_list:
        return list(itertools.chain.from_iterable(output['holidays'].to_list()))
    else:
        return output.drop('holidays', axis=1)


def _get_holidays(*, country: ListorStr, extent: ListorStr, **kwargs) -> pd.DataFrame:
    """ Get a list of holidays for the area of interest """

    country = _validate_inputs(country, ['ES', 'PT'])
    extent = _validate_inputs(extent, ['national', 'regional'])

    selected_regional = _select_regional(country, **kwargs) if 'regional' in extent else []

    holidays = HOLIDAYS[(HOLIDAYS.country.isin(country)) & (HOLIDAYS.extent.isin(extent))]
    holidays = holidays[~((holidays.extent == 'regional') &
                        ~(holidays.index.isin(selected_regional)))]

    return holidays


def to_datetime(d: datetime) -> datetime:
    """ Convert date objects to datetime. """
    return datetime(d.year, d.month, d.day)


def _calculate_holiday(year: int, check: str, keys: List[int]) -> datetime:
    """ Calculate the holiday for a given year.

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

    if check == 'f':  # fix days
        return datetime(year, keys[0], keys[1])
    elif check == 'e':  # holidays calculated based on easter day
        return to_datetime(easter(year))+timedelta(days=keys[0])
    elif check == 'm':  # moving holidays
        return to_datetime(CLD.monthdatescalendar(year, keys[0])[keys[1]][keys[2]])
    elif check == 's':  # special case from 'lousada'
        return datetime(year, 7, max(w[-1] for w in calendar.monthcalendar(year, 7)))\
               + timedelta(days=1)
    else:
        return None


def check_holidays(method):
    """ Check if the object in Holidays has any holidays calculated before. """
    @wraps(method)
    def wrapper(*args, **kwargs):
        if args[0].holidays is None:
            raise Exception('No holidays have been calculated for the date range')
        else:
            return method(*args, **kwargs)
    return wrapper


class Holidays:
    """ Class to generate the holidays dates for a period of time.

    Examples
    --------
    >>> from holidays import Holidays
    >>> hol = holidays.Holidays('2021-01-01', '2021-12-31')
    >>> hol.calculate(country='PT', extent=['national'])
    Holidays(start_date=2021-01-01, end_date=2021-12-31)
    >>> hol.as_table()
    country	extent	 label	                      calculate	                               date
    PT     national Ano Novo	                january 1st                              2021-01-01
    PT	   national Carnaval	                47 days before easter sunday on a tuesday 2021-02-16
    PT	   national Sexta-Feira Santa	        friday right before easter sunday        2021-04-02
    PT	   national Pascoa	                    easter sunday                            2021-04-04
    PT	   national 25 de Abril	                april 25th                               2021-04-25
    PT	   national Dia do Trabalhador	        may 1th                                  2021-05-01
    PT	   national Corpo de Deus               60 days after easter sunday, on a thursday 2021-06-03
    PT	   national Dia de Portugal	            june 10th	                             2021-06-10
    PT	   national Assuncao Maria	            august 15th                              2021-08-15
    PT	   national Implatacao da Republica     october 5th                              2021-10-05
    PT	   national Todos os Santos	            november 1st                             2021-11-01
    PT	   national Restauracao da Independencia december 1st                            2021-12-01
    PT	   national Imaculada Conceicao         december 8th                             2021-12-08
    PT	   national Natal                       december 25th                            2021-12-25
    """

    def __init__(self, start_date: str, end_date: str, date_format: str = '%Y-%m-%d') -> None:
        """ Define date period to calculate the holidays.

        Parameters
        ----------
        start_date : str, '%Y-%m-%d' (ex:2020-05-15)
            start of the period in the format
        end_date : str, '%Y-%m-%d' (ex:2020-05-15)
            end of the period
        date_format : str, default='%Y-%m-%d'
            string describing th date format used
        """

        self.start_date = start_date
        self.end_date = end_date
        self._date_format = date_format

        self._start_date: datetime = datetime.strptime(start_date, self._date_format)
        self._end_date: datetime = datetime.strptime(end_date, self._date_format)

        self.years: Set[int] = set(
            [self._start_date.year] + list(range(self._start_date.year, self._end_date.year+1))
        )

        self.holidays: Optional[pd.DataFrame] = None

    def __repr__(self) -> str:
        return f'Holidays(start_date={self.start_date}, end_date={self.end_date})'

    @check_holidays
    def __len__(self) -> int:
        """ Return count of holidays in the date range. """
        return int(self.holidays.shape[0])

    def __contains__(self, item: str) -> bool:
        """ Check whether a date is between the given range. """
        return self._start_date <= datetime.strptime(item, self._date_format) <= self._end_date

    def calculate(self, **kwargs) -> None:
        """ Calculate the holidays for the select time period """

        self._holidays = _get_holidays(**kwargs)

        self.holidays = pd.concat([self._holidays.copy().assign(year=y) for y in self.years])

        self.holidays['date'] = self.holidays.apply(
            lambda x: _calculate_holiday(x['year'], x['type'], x['codes']), axis=1
        )

        self.holidays = self.holidays.drop(['type', 'codes', 'year'], axis=1)

        self.holidays = self.holidays[
            (self.holidays.date >= self._start_date) & (self.holidays.date <= self._end_date)
        ]

        self.holidays = self.holidays.sort_values('date').reset_index(drop=True)

    def _select_cols(self, *, drop: List[str] = []) -> pd.DataFrame:
        """ Drop any columns that are not needed """
        columns = {'country', 'extent', 'label', 'calculate'}
        if drop:
            if set(drop).issubset(columns):
                return self.holidays.copy().drop(columns=drop)
            else:
                raise Exception(f' Value {drop} is not a valid column')
        else:
            return self.holidays

    @check_holidays
    def as_table(self, **kwargs) -> pd.DataFrame:
        """ Returns calculated holidays as a pandas dataframe. """
        return self._select_cols(**kwargs)

    @check_holidays
    def as_list(self, date_str: bool = True, **kwargs) -> List[List[str]]:
        """ Returns calculated holidays a a list of dated in string format. """

        output = self._select_cols(**kwargs)

        if date_str:
            output['date'] = output['date'].dt.strftime(self._date_format)

        return output.to_numpy().tolist()

    @check_holidays
    def as_time_series(self, sep_region: bool = False, hot_encode: bool = False) -> pd.DataFrame:
        """ Returns holidays as a time series were the dates of holidays are
        a variable called holiday with the value of 1.

        Parameters
        ----------
        sep_region : bool, default=False
            To assign a lower value to regional holidays
        hot_encode : bool, default=False
            Display holidays as features and hot encoded

        Notes
        -----
        If sep_region is True regional holidays will have a value of 0.5 while
        national will stay at 1.
        """

        _columns = ['date', 'extent', 'label']

        output = pd.concat([
            pd.DataFrame([(self._start_date, '', ''), (self._end_date, '', '')], columns=_columns),
            self.holidays[_columns],
        ]).set_index('date').resample('1D').sum().replace('', 0)

        if hot_encode:
            return pd.get_dummies(output['label']).drop(columns=[0])
        else:
            output['holiday'] = output['label'].where(
                (output['label'] == 0) | (output['label'] == ''), 1)
            if sep_region:
                output['holiday'] = output.apply(
                    lambda x: 0.5 if x['extent'] == 'regional' else x['holiday'],
                    axis=1
                )
            return output[['holiday']]

    def working_days(self, freq: str = 'W') -> pd.DataFrame:
        """ Estimate the number of working/business days in period of time
        specified by the param freq.

        Parameters
        ----------
        freq : str, default='W'
            frequency of the timeframe

        Notes
        -----
        Acepted values are 'W' - week, 'M' - month, 'Y' - year (pandas).
        """

        if freq in ['W', 'M', 'Y']:
            if self.holidays is None:
                # if no holidays to be included in the timeseries
                table = pd.DataFrame(index=pd.date_range(self._start_date, self._end_date),
                                     columns=['holiday'], data=0)
            else:
                table = self.as_time_series()
            # remove holidays and weekends
            table = table[(table['holiday'] != 1) & (table.index.weekday < 5)]
            return (table.groupby(pd.Grouper(freq=freq))
                         .count()
                         .rename(columns={'holiday': 'business_days'}))
        else:
            raise Exception('Freq input not reconized, please choose W: week, M: month, Y: year')

    def leap_years(self) -> Dict[int, bool]:
        """ Check if years are leap years or not. """
        return {i: calendar.isleap(i) for i in self.years}

    @staticmethod
    def list_regional(*args, **kwargs):
        """ Return table with available regional holidays """
        return _select_regional(*args, as_list=False, **kwargs)
