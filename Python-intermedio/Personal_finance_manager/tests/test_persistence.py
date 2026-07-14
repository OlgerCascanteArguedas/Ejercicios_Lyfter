import json
import tempfile
import unittest
from pathlib import Path

from persistence import load_data


class TestPersistence(unittest.TestCase):

    def test_load_data_returns_list_from_valid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "data.json"
            expected_data = [{"name": "Food"}]

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(expected_data, file)

            self.assertEqual(
                load_data(file_path),
                expected_data
            )

    def test_load_data_returns_empty_list_for_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "data.json"

            with open(file_path, "w", encoding="utf-8") as file:
                file.write("{")

            self.assertEqual(
                load_data(file_path),
                []
            )

    def test_load_data_returns_empty_list_for_unexpected_json_format(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "data.json"

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump({"name": "Food"}, file)

            self.assertEqual(
                load_data(file_path),
                []
            )


if __name__ == "__main__":
    unittest.main()
