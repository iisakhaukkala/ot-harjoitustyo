from database_connection import get_database_connection


def drop_tables(connection):
    connection.execute("DROP TABLE IF EXISTS Members")


def create_tables(connection):
    connection.execute(
        '''CREATE TABLE Member (
        username TEXT PRIMARY KEY,
        password TEXT,
        name TEXT,
        email TEXT,
        phone TEXT,
        membership TEXT,
        admin BOOLEAN)''')


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
