import unittest

from holidays_pt.regions import _check_exists, ls_districts, select


class TestRegions(unittest.TestCase):
    def test_check_exists_pass(self):
        self.assertIsNone(_check_exists(ls_districts, ["aveiro"]))

    def test_select(self):
        to_check = {
            "ptr0001",
            "ptr0002",
            "ptr0003",
            "ptr0004",
            "ptr0005",
            "ptr0006",
            "ptr0007",
            "ptr0008",
            "ptr0009",
            "ptr0010",
            "ptr0011",
            "ptr0012",
            "ptr0013",
            "ptr0014",
            "ptr0015",
            "ptr0016",
            "ptr0031",
        }
        self.assertEqual(select(district=["aveiro"], county=["braganca"]), to_check)


if __name__ == "__main__":
    unittest.main()
