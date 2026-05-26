import unittest
from src.Ejercicios_de_Funciones_4 import reverse_string


class TestReverseString(unittest.TestCase):

    # Caso 1
    def test_reverse_normal_word(self):
        result = reverse_string("python")
        self.assertEqual(result, "nohtyp")

    # Caso 2
    def test_reverse_empty_string(self):
        result = reverse_string("")
        self.assertEqual(result, "")

    # Caso 3
    def test_reverse_sentence(self):
        result = reverse_string("hello world")
        self.assertEqual(result, "dlrow olleh")


if __name__ == "__main__":
    unittest.main()
