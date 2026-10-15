
# Personal Expense Tracker
# Daily Expense Report

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount (UGX): "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_report():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== DAILY EXPENSE REPORT =====")

    total = 0

    for expense in expenses:
        print(
            f"{expense['name']} - "
            f"{expense['category']} - "
            f"UGX {expense['amount']:,.0f}"
        )
        total += expense["amount"]

    print("-------------------------------")
    print(f"Total expenses: UGX {total:,.0f}")

def main():
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Daily Report")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_report()
        elif choice == "3":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
