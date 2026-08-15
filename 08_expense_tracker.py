# Simple Expense Tracker

expenses = []


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("\nNo expenses recorded.")
        return

    print("\n--- Expenses ---")

    total = 0

    for expense in expenses:
        print(expense["name"], "₹", expense["amount"])
        total += expense["amount"]

    print("----------------")
    print("Total: ₹", total)


while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice.")