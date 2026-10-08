# Expense Tracker

A Flask web app for managing personal expenses using Python, SQLite, HTML and CSS. Users can add, view, edit and delete expenses, with a simple dashboard showing total expenses and the number of recorded expenses.

## Requirements

- Python 3.9+
- Flask

## Run it

```bash
git clone https://github.com/nikhilmunimakula/expense-tracker.git
cd expense-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000

## Features

- Add Expenses
- View Expenses
- Edit Expenses
- Delete Expenses
- Expense Categories
- Automatic expense dates
- Total Expense Summary
- Expense Count Dashboard

## How it works

User Input → Flask → SQLite Database → CRUD Operations → Jinja Templates → HTML/CSS Interface
