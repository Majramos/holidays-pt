import unittest
from datetime import datetime

from holidays_pt.utils import Weekday, easter, flatten


class TestUtils(unittest.TestCase):
    def test_weekday_value(self):
        self.assertEqual(Weekday.TUESDAY.value, 2)

    def test_weekday_name(self):
        self.assertEqual(Weekday(3).name, "WEDNESDAY")

    def test_easter(self):
        self.assertEqual(easter(2020), datetime(2020, 4, 12, 0, 0))

    def test_flatten(self):
        self.assertEqual(flatten([["a", "b"], ["c", "d"]]), ["a", "b", "c", "d"])


if __name__ == "__main__":
    unittest.main()
