from pathlib import Path
import sqlite3

def get_connection():
    return sqlite3.connect("app/data/aios.db")

def create_tables():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
    CREATE TABLE IF NOT EXISTs conversation(id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    conn.close()

create_tables()