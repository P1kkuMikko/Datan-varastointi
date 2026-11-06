#TODO: 

import sqlite3

from pathlib import Path

DB_PATH = Path("sqlite_books.db")

def create_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL)""")

    connection.commit()
    connection.close()


def add_data(books_dict):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    for title, details in books_dict.items():
        cursor.execute("""
            INSERT INTO books (title, author, pages)
            VALUES (?, ?, ?)
        """, (title, details["author"], details["pages"]))
        
    connection.commit()
    connection.close()

def query_data(limit):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    if limit <= 0:
        connection.close()
        return []

    cursor.execute("""
        SELECT title, author, pages
        FROM books
        ORDER BY pages DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    connection.close()
    return rows