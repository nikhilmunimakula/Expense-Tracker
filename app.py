from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)


def connect_database():
    return sqlite3.connect("expenses.db")


@app.route("/")
def home():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expense = cursor.fetchone()[0]

    if total_expense is None:
        total_expense = 0

    cursor.execute("SELECT COUNT(*) FROM expenses")
    expense_count = cursor.fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        expenses=expenses,
        total_expense=total_expense,
        expense_count=expense_count
    )

@app.route("/add", methods=["POST"])
def add_expense():
    amount = float(request.form["amount"])
    category = request.form["category"]
    description = request.form["description"]

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date.today()))

    connection.commit()
    connection.close()

    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete_expense(id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")

@app.route("/edit/<int:id>")
def edit_expense(id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (id,)
    )

    expense = cursor.fetchone()

    connection.close()

    return render_template("edit.html", expense=expense)


@app.route("/update/<int:id>", methods=["POST"])
def update_expense(id):
    amount = float(request.form["amount"])
    category = request.form["category"]
    description = request.form["description"]

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?
        WHERE id = ?
    """, (amount, category, description, id))

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)