
from collections import defaultdict


class Reports:

    def __init__(self, transactions):
        self.transactions = transactions

    def show_summary(self):
        income = sum(
            t["amount"] for t in self.transactions
            if t["transaction_type"] == "Income"
        )

        expenses = sum(
            t["amount"] for t in self.transactions
            if t["transaction_type"] == "Expense"
        )

        print("\n========== FINANCIAL SUMMARY ==========")
        print(f"Total Income: Rs.{income:.2f}")
        print(f"Total Expenses: Rs.{expenses:.2f}")
        print(f"Current Balance: Rs.{income - expenses:.2f}")

    def category_report(self):
        categories = defaultdict(float)

        for t in self.transactions:
            if t["transaction_type"] == "Expense":
                categories[t["category"]] += t["amount"]

        print("\n========== CATEGORY REPORT ==========")

        if not categories:
            print("No expenses available.")
            return

        for category, amount in categories.items():
            print(f"{category}: Rs.{amount:.2f}")

    def monthly_report(self):
        monthly = defaultdict(float)

        for t in self.transactions:
            if t["transaction_type"] == "Expense":
                month = t["date"][:7]
                monthly[month] += t["amount"]

        print("\n========== MONTHLY EXPENSE REPORT ==========")

        if not monthly:
            print("No expenses available.")
            return

        for month, amount in sorted(monthly.items()):
            print(f"{month}: Rs.{amount:.2f}")
