from typing import Self


class Year(int):
    MIN: int = 1
    MAX: int = 9999

    def __new__(cls, value: int) -> Self:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"year must be an int, got {type(value).__name__}")
        if not cls.MIN <= value <= cls.MAX:
            raise ValueError(f"year must be between {cls.MIN} and {cls.MAX}, got {value}")
        return super().__new__(cls, value)

    def __repr__(self) -> str:
        return f"Year({int(self)})"
