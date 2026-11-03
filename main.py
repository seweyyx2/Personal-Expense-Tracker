
from tracker import ExpenseTracker
from reports import Reports


def main():

    tracker = ExpenseTracker()

    while True:

        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. Financial Summary")
        print("6. Category-wise Report")
        print("7. Monthly Expense Report")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice in ("1", "2"):

            try:
                amount = float(input("Enter amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

                category = input("Enter category: ").strip()
                description = input("Enter description: ").strip()

                if not category or not description:
                    print("Category and description cannot be empty.")
                    continue

                transaction_type = "Income" if choice == "1" else "Expense"

                tracker.add_transaction(
                    amount, category, description, transaction_type
                )

            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":
            tracker.view_transactions()

        elif choice == "4":
            tracker.view_transactions()
            transaction_id = input("\nEnter transaction ID to delete: ")
            tracker.delete_transaction(transaction_id)

        elif choice == "5":
            Reports(tracker.get_transactions()).show_summary()

        elif choice == "6":
            Reports(tracker.get_transactions()).category_report()

        elif choice == "7":
            Reports(tracker.get_transactions()).monthly_report()

        elif choice == "8":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    main()
