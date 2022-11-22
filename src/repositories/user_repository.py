from database_connection import get_database_connection

def create_user(username = str, password = str):
    connection = get_database_connection()
    connection.execute("INSERT INTO Members (username, password) VALUES (?, ?)", [username, password])

def get_users():
    connection = get_database_connection()
    users = connection.execute("SELECT username FROM Members").fetchall()
    return users