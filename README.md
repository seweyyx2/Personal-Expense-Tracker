# Personal Expense Tracker

A simple command-line based Personal Expense Tracker built using Python. This application helps users manage their income and expenses, track their balance, and generate financial reports.

## Features

- Add income transactions
- Add expense transactions
- View all transactions
- Delete transactions
- Calculate total income and expenses
- Display current account balance
- Generate category-wise expense reports
- Generate monthly expense reports
- Store transaction data using JSON for future use

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling

## Project Structure

```text
Personal-Expense-Tracker/
│
├── data/
│   └── transactions.json
│
├── main.py
├── transaction.py
├── tracker.py
├── storage.py
├── reports.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Personal-Expense-Tracker.git
```

2. Navigate to the project directory:

```bash
cd Personal-Expense-Tracker
```

3. Make sure Python 3 is installed.

4. Run the application:

```bash
python main.py
```

## Application Menu

The application provides the following options:

1. Add Income
2. Add Expense
3. View Transactions
4. Delete Transaction
5. Financial Summary
6. Category-wise Report
7. Monthly Expense Report
8. Exit

## Data Storage

All transactions are stored locally in JSON format inside the `data` directory.

The application automatically loads previously saved transactions when restarted.

## Future Improvements

- Graphical user interface
- Expense visualization using charts
- Monthly budget management
- Transaction search and filtering
- Export reports to CSV

## Author

Developed as a Python learning project to practise programming, file handling, and object-oriented programming concepts.    