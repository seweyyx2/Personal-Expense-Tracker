
from datetime import datetime


class Transaction:
    def __init__(self, amount, category, description, transaction_type):
        self.id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.transaction_type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "transaction_type": self.transaction_type,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            data["amount"],
            data["category"],
            data["description"],
            data["transaction_type"]
        )._restore_id(data)

    def _restore_id(self, data):
        self.id = data["id"]
        self.date = data["date"]
        return self
