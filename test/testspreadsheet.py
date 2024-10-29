from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_invalid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "4.2")
        # Evaluate a given cell (e.g., the evaluation of "A1" is "42").
        self.assertEqual("#Error", spreadsheet.evaluate("B1"))

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "42")
        # Evaluate a given cell (e.g., the evaluation of "A1" is "42").
        self.assertEqual(42, spreadsheet.evaluate("B1"))
