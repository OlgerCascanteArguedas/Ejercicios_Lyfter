import unittest
from src.Ejercicios_de_Funciones_3 import sum_list


class TestSumList(unittest.TestCase):

    def test_sum_small_list(self):
        result = sum_list([1, 2, 3, 4])
        self.assertEqual(result, 10)

    def test_sum_empty_list(self):
        result = sum_list([])
        self.assertEqual(result, 0)

    def test_sum_negative_numbers(self):
        result = sum_list([-1, -2, 3])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
