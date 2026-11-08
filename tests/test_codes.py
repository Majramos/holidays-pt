import unittest

from holidays_pt.codes import select


class TestCodes(unittest.TestCase):
    def test_select(self):
        to_check = [
            {
                "extent": "national",
                "label": "Ano Novo",
                "type": "f",
                "codes": [1, 1, 0],
                "calculate": "january 1st",
            },
            {
                "extent": "national",
                "label": "Sexta-Feira Santa",
                "type": "e",
                "codes": [-2, 0, 0],
                "calculate": "friday right before easter sunday",
            },
            {
                "extent": "regional",
                "label": "Sao Tome",
                "type": "f",
                "codes": [7, 25, 0],
                "calculate": "july 25th",
            },
            {
                "extent": "regional",
                "label": "Elevacao Sines a vila (1362)",
                "type": "f",
                "codes": [11, 24, 0],
                "calculate": "november 24th",
            },
        ]

        self.assertEqual(
            select(codes=["ptn0001", "ptn0003", "ptr0051", "ptr0136"]), to_check
        )


if __name__ == "__main__":
    unittest.main()
