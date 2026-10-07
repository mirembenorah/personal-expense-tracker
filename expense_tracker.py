# Personal Expense Tracker
# This program allows a user to record expenses
# and calculate the total amount spent.

expenses = []


def add_expense():
    """Add a new expense."""
    item = input("Enter expense name: ")
    amount = float(input("Enter amount spent: "))

    expense = {
        "item": item,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!\n")


def view_expenses():
    """Display all recorded expenses."""

    if len(expenses) == 0:
        print("No expenses recorded yet.\n")
        return

    print("\n--- Your Expenses ---")

    for number, expense in enumerate(expenses, start=1):
        print(
            number,
            "-",
            expense["item"],
            ":",
            expense["amount"]
        )

    print()


def calculate_total():
    """Calculate total money spent."""

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total amount spent:", total)
    print()


def main():

    while True:

        print("===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.\n")


main()
