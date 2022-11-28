from database_connection import get_database_connection


class RegisterRepository:
    def __init__(self, connection):
        self._connection = connection

    
    def create_user(self, username=str, password=str, name=str, email=str, phone=str, memberhip=str, admin=int):
        self._connection.execute("INSERT INTO Members (username, password, name, email, phone, membership, admin) VALUES (?, ?, ?, ?, ?, ?, ?)", [
                       username, password, name, email, phone, memberhip, admin])


    def get_users(self):
        users = self._connection.execute("SELECT username FROM Members").fetchall()
        return users


    def delete_all(self):
        pass

    
register_repository = RegisterRepository(get_database_connection())