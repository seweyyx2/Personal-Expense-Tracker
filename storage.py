
import json
import os

FILE_PATH = "data/transactions.json"


def load_data():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_data(transactions):
    os.makedirs("data", exist_ok=True)

    with open(FILE_PATH, "w") as file:
        json.dump(transactions, file, indent=4)
