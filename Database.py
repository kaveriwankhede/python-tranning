import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'linkkiwi2026'  # needed for flash messages


def get_db():
    conn = sqlite3.connect('myproject.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS SCORE (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Student_name TEXT NOT NULL,
            total_marks INTEGER NOT NULL,
            exam_date DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()  # function call
    app.run(debug=True)