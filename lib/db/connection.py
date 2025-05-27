import sqlite3

def get_connection():
    conn = sqlite3.connect('articles.db')
    # access columns by rows
    conn.row_factory = sqlite3.Row 
    return conn