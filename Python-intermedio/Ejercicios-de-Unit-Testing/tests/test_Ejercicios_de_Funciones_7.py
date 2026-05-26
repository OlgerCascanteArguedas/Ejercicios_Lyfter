import unittest
from src.Ejercicios_de_Funciones_7 import get_prime_numbers


class TestGetPrimeNumbers(unittest.TestCase):

    # Caso 1
    def test_prime_numbers_in_list(self):

        result = get_prime_numbers(
            [1, 4, 6, 7, 13, 9, 67]
        )

        self.assertEqual(
            result,
            [7, 13, 67]
        )

    # Caso 2
    def test_list_without_prime_numbers(self):

        result = get_prime_numbers(
            [1, 4, 6, 8, 9, 10]
        )

        self.assertEqual(
            result,
            []
        )

    # Caso 3
    def test_all_prime_numbers(self):

        result = get_prime_numbers(
            [2, 3, 5, 7, 11]
        )

        self.assertEqual(
            result,
            [2, 3, 5, 7, 11]
        )


if __name__ == "__main__":
    unittest.main()
