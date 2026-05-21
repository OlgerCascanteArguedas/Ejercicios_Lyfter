import unittest
from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_small_list(self):
        result = bubble_sort([5, 3, 1, 4, 2])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_large_list(self):
        numbers = list(range(150, 0, -1))
        result = bubble_sort(numbers)
        self.assertEqual(result, list(range(1, 151)))

    def test_empty_list(self):
        result = bubble_sort([])
        self.assertEqual(result, [])

    def test_invalid_parameter(self):
        with self.assertRaises(TypeError):
            bubble_sort("hola")


if __name__ == "__main__":
    unittest.main()
