import unittest
from src.Ejercicios_de_Funciones_6 import sort_hyphen_words


class TestSortHyphenWords(unittest.TestCase):

    # Caso 1
    def test_sort_normal_words(self):
        result = sort_hyphen_words(
            "python-variable-funcion"
        )

        self.assertEqual(
            result,
            "funcion-python-variable"
        )

    # Caso 2
    def test_sort_single_word(self):
        result = sort_hyphen_words("python")

        self.assertEqual(
            result,
            "python"
        )

    # Caso 3
    def test_sort_multiple_words(self):
        result = sort_hyphen_words(
            "zebra-monitor-computadora"
        )

        self.assertEqual(
            result,
            "computadora-monitor-zebra"
        )


if __name__ == "__main__":
    unittest.main()
