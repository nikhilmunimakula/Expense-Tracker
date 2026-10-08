import sqlite3
from datetime import date


def connect_database():
    return sqlite3.connect("expenses.db")


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date.today()))

    connection.commit()
    connection.close()

    print("Expense added successfully!")


def view_expenses():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    connection.close()

    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n----- Your Expenses -----")

        for expense in expenses:
            print(
                f"ID: {expense[0]} | "
                f"Date: {expense[4]} | "
                f"Amount: ₹{expense[1]:.2f} | "
                f"Category: {expense[2]} | "
                f"Description: {expense[3]}"
            )


def view_total():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    connection.close()

    if total is None:
        total = 0

    print(f"Total Expenses: ₹{total:.2f}")


def update_expense():
    expense_id = int(input("Enter the ID of the expense to update: "))

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if expense is None:
        print("Expense not found.")
        connection.close()
        return

    print("\nCurrent Expense:")
    print(f"Amount: ₹{expense[1]:.2f}")
    print(f"Category: {expense[2]}")
    print(f"Description: {expense[3]}")

    amount = float(input("Enter new amount: "))
    category = input("Enter new category: ")
    description = input("Enter new description: ")

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
    """, (amount, category, description, expense_id))

    connection.commit()
    connection.close()

    print("Expense updated successfully!")


def delete_expense():
    expense_id = int(input("Enter the ID of the expense to delete: "))

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if expense is None:
        print("Expense not found.")
        connection.close()
        return

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()
    connection.close()

    print("Expense deleted successfully!")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "4":
        update_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")