from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_formula_with_arithmetic_operator_sum_mult(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=1+3*2")
        self.assertEqual(7, spreadsheet.evaluate("A1"))

    def test_evaluate_formula_with_arithmetic_operator_division_by_zero(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_with_arithmetic_operator_sum_and_bad_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_with_arithmetic_operator_sum(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=1+3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_evaluate_formula_reference_circular(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_reference_bad_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=B1")
        spreadsheet.set("B1", "42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_reference_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",    "=B1")
        spreadsheet.set("B1", "42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))


    def test_evaluate_formula_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",   "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_formula_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",  "=1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_formula_wrong_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1",  "='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_string_2(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "Apple'")
        # Evaluate matching quotes
        self.assertEqual("#Error", spreadsheet.evaluate("B1"))

    def test_evaluate_invalid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "'Apple")
        # Evaluate matching quotes
        self.assertEqual("#Error", spreadsheet.evaluate("B1"))


    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("B1", "'Apple'")
        # Evaluate a given cell (e.g., the evaluation of "A1" is "42").
        self.assertEqual("Apple", spreadsheet.evaluate("B1"))


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
