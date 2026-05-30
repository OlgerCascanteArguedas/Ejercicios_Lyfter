import unittest
from unittest.mock import mock_open, patch
from src.file_reader import read_lines


class TestReadLines(unittest.TestCase):

    def test_read_lines_returns_expected_content(self):
        fake_content = "Hola\nMundo\n"

        with patch("builtins.open", mock_open(read_data=fake_content)):
            result = read_lines("archivo.txt")

        self.assertEqual(result, ["Hola\n", "Mundo\n"])

    def test_read_lines_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                read_lines("archivo_inexistente.txt")


if __name__ == "__main__":
    unittest.main()
