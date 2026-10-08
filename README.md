Expense Tracker

A Flask web app for managing personal expenses using Python, MySQL, HTML and CSS. Users can add, view, edit and delete expenses, with a simple dashboard showing total expenses and the number of recorded expenses.

Requirements

Python 3.9+

Flask

Run it

git clone https://github.com/nikhilmunimakula/expense-tracker.git
cd expense-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Open http://127.0.0.1:5000

Features

Add expenses

View expenses

Edit expenses

Delete expenses

Expense categories

Automatic expense dates

Total expense summary

Expense count dashboard

How it works

User Input → Flask → SQLite Database → CRUD Operations → Jinja Templates → HTML/CSS Interface

Technologies Used

Python · Flask · SQLite · HTML · CSS 