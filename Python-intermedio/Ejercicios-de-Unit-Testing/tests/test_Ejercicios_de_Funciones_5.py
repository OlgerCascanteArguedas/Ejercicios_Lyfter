import unittest
from src.Ejercicios_de_Funciones_5 import count_case_letters


class TestCountCaseLetters(unittest.TestCase):

    # Caso 1
    def test_mixed_letters(self):
        result = count_case_letters("Hello World")
        self.assertEqual(result, (2, 8))

    # Caso 2
    def test_all_uppercase(self):
        result = count_case_letters("PYTHON")
        self.assertEqual(result, (6, 0))

    # Caso 3
    def test_all_lowercase(self):
        result = count_case_letters("python")
        self.assertEqual(result, (0, 6))


if __name__ == "__main__":
    unittest.main()
