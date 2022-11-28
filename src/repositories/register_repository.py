from database_connection import get_database_connection


class RegisterRepository:
    def __init__(self, connection):
        self._connection = connection

    
    def create_user(self, username=str, password=str, name=str, email=str, phone=str, memberhip=str, admin=int):
        self._connection.execute("INSERT INTO Members (username, password, name, email, phone, membership, admin) VALUES (?, ?, ?, ?, ?, ?, ?)", [
                       username, password, name, email, phone, memberhip, admin])


    def edit_name(self):
        pass


    def edit_email(self):
        pass


    def edit_phone(self):
        pass


    def make_admin(self):
        pass


    def unmake_admin(self):
        pass


    def get_all(self):
        return self._connection.execute("SELECT * FROM Members").fetchall()
        

    def find_by_username(self, username): 
        return self._connection.execute("SELECT * FROM Members WHERE username = ?", [username]).fetchone()
        

    def find_by_name(self): # admin
        pass


    def edit_membership(self): # admin
        pass


    def delete_all(self):
        self._connection.execute("DELETE FROM Members")

    
register_repository = RegisterRepository(get_database_connection())