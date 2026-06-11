import json
import os


def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


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
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
