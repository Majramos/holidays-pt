from enum import Enum
from typing import Self


class Weekday(Enum):
    """Weeks days according to the iso norm"""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class Year(int):
    """Year bounded by the easter function"""

    MIN: int = 1583
    MAX: int = 4099

    def __new__(cls, value: int) -> Self:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"year must be an int, got {type(value).__name__}")
        if not cls.MIN <= value <= cls.MAX:
            raise ValueError(
                f"year must be between {cls.MIN} and {cls.MAX}, got {value}"
            )
        return super().__new__(cls, value)

    def __repr__(self) -> str:
        return f"Year({int(self)})"
