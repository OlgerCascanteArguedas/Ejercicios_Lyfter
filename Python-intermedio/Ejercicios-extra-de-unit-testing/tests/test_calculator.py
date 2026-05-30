import unittest
from src.calculator import divide


class TestDivide(unittest.TestCase):

    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_with_string(self):
        with self.assertRaises(TypeError):
            divide("10", 2)


if __name__ == "__main__":
    unittest.main()
