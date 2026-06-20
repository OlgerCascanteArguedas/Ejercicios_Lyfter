import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

CATEGORIES_FILE = DATA_DIR / "categories.json"
TRANSACTIONS_FILE = DATA_DIR / "transactions.json"


def create_data_folder():
    DATA_DIR.mkdir(exist_ok=True)


def save_data(file_path, data):
    create_data_folder()

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_data(file_path):
    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []

    except TypeError:
        return []
