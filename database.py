import sqlite3

DATABASE = "students.db"

def connect():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        matric TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        department TEXT,
        faculty TEXT,
        age INTEGER
    )
    """)

    conn.commit()
    conn.close()