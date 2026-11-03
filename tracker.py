
from transaction import Transaction
from storage import load_data, save_data


class ExpenseTracker:

    def __init__(self):
        self.transactions = load_data()

    def add_transaction(self, amount, category, description, transaction_type):
        transaction = Transaction(
            amount, category, description, transaction_type
        )

        self.transactions.append(transaction.to_dict())
        save_data(self.transactions)

        print("\nTransaction added successfully!")

    def view_transactions(self):
        if not self.transactions:
            print("\nNo transactions found.")
            return

        print("\n========== TRANSACTIONS ==========")

        for t in self.transactions:
            print(f"\nID: {t['id']}")
            print(f"Type: {t['transaction_type']}")
            print(f"Amount: Rs.{t['amount']:.2f}")
            print(f"Category: {t['category']}")
            print(f"Description: {t['description']}")
            print(f"Date: {t['date']}")

    def delete_transaction(self, transaction_id):
        original_count = len(self.transactions)

        self.transactions = [
            t for t in self.transactions if t["id"] != transaction_id
        ]

        if len(self.transactions) < original_count:
            save_data(self.transactions)
            print("\nTransaction deleted successfully!")
        else:
            print("\nTransaction ID not found.")

    def get_transactions(self):
        return self.transactions
