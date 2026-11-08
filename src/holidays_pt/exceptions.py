class HolidaysPTError(Exception):
    """Base exeception for Holidays PT"""


class MissingLocationError(HolidaysPTError):
    """Requires either district or county"""


class MissingColumnError(HolidaysPTError):
    """Either the name of the column is wrong or the column does not exist"""


class NoBankHolidaysError(HolidaysPTError):
    """No holidays have been calculated for the date range"""
