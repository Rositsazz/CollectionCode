import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

create_users_table = """
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                   phone TEXT, email TEXT unique, password TEXT)
"""

cursor.execute(create_users_table)
connection.commit()
