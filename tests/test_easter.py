from datetime import datetime

import pytest

from holidays_pt._easter import calculate_easter
from holidays_pt.models import Year

KNOWN_EASTERS = [
    (1583, (4, 10)),
    (1600, (4, 2)),
    (1700, (4, 11)),
    (1761, (3, 22)),  # earliest possible date
    (1818, (3, 22)),  # earliest possible date
    (1886, (4, 25)),  # latest possible date
    (1900, (4, 15)),
    (1943, (4, 25)),  # latest possible date
    (1954, (4, 18)),
    (1992, (4, 19)),
    (2000, (4, 23)),
    (2010, (4, 4)),
    (2018, (4, 1)),
    (2019, (4, 21)),
    (2020, (4, 12)),
    (2021, (4, 4)),
    (2022, (4, 17)),
    (2023, (4, 9)),
    (2024, (3, 31)),
    (2025, (4, 20)),
    (2026, (4, 5)),
    (2027, (3, 28)),
    (2028, (4, 16)),
    (2038, (4, 25)),
    (2100, (3, 28)),
    (2285, (3, 22)),  # earliest possible date
]


@pytest.mark.parametrize(("year", "expected"), KNOWN_EASTERS)
def test_easter_known_dates(year: int, expected: tuple[int, int]) -> None:
    month, day = expected
    assert calculate_easter(Year(year)) == datetime(year, month, day)


def test_easter_returns_datetime_at_midnight() -> None:
    result = calculate_easter(Year(2026))
    assert isinstance(result, datetime)
    assert (result.hour, result.minute, result.second, result.microsecond) == (
        0,
        0,
        0,
        0,
    )
    assert result.tzinfo is None


@pytest.mark.parametrize("year", range(1583, 4100))
def test_easter_is_always_sunday(year: int) -> None:
    assert calculate_easter(Year(year)).weekday() == 6


@pytest.mark.parametrize("year", range(1583, 4100))
def test_easter_within_possible_range(year: int) -> None:
    result = calculate_easter(Year(year))
    assert result.year == year
    assert (3, 22) <= (result.month, result.day) <= (4, 25)


def test_easter_accepts_year_subclass_of_int() -> None:
    assert calculate_easter(Year(2026)) == calculate_easter(Year(2026) + 0)  # type: ignore[arg-type]


def test_year_validation_prevents_invalid_input() -> None:
    with pytest.raises(ValueError):
        calculate_easter(Year(0))
    with pytest.raises(ValueError):
        calculate_easter(Year(10000))
