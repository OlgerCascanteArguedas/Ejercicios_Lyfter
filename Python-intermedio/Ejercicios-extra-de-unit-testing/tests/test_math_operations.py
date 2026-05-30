import unittest
from src.math_operations import MathOperations


class TestMathOperations(unittest.TestCase):

    def setUp(self):
        self.math = MathOperations()

    # -------------------------
    # POSITIVE NUMBERS TESTS
    # -------------------------

    def test_add_positive_numbers(self):
        result = self.math.add(5, 3)
        self.assertEqual(result, 8)

    def test_average_positive_numbers(self):
        result = self.math.average([2, 4, 6])
        self.assertEqual(result, 4)

    def test_multiply_positive_numbers(self):
        result = self.math.multiply(2, 5)
        self.assertEqual(result, 10)

    # -------------------------
    # NEGATIVE NUMBERS TESTS
    # -------------------------

    def test_add_negative_numbers(self):
        result = self.math.add(-5, -3)
        self.assertEqual(result, -8)

    def test_average_negative_numbers(self):
        result = self.math.average([-2, -4, -6])
        self.assertEqual(result, -4)

    def test_multiply_negative_numbers(self):
        result = self.math.multiply(-2, -5)
        self.assertEqual(result, 10)

    # -------------------------
    # ZERO TESTS
    # -------------------------

    def test_add_zeros(self):
        result = self.math.add(0, 0)
        self.assertEqual(result, 0)

    def test_average_zeros(self):
        result = self.math.average([0, 0, 0])
        self.assertEqual(result, 0)

    def test_multiply_zeros(self):
        result = self.math.multiply(0, 5)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
