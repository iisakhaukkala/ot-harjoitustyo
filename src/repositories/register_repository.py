from database_connection import get_database_connection


class RegisterRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(  # pylint: disable=too-many-arguments
            self, username=str,
            password=str,
            name=str,
            email=str,
            phone=str,
            memberhip=str,
            admin=int):
        self._connection.execute(
            '''INSERT INTO Members
            (username, password, name, email, phone, membership, admin)
            VALUES (?, ?, ?, ?, ?, ?, ?)''', [
                username, password, name, email, phone, memberhip, admin])

    def edit_name(self, name, username):
        self._connection.execute(
            "UPDATE Members SET name = ? WHERE username = ?", [name, username])

    def edit_email(self, email, username):
        self._connection.execute(
            "UPDATE Members SET email = ? WHERE username = ?", [email, username])

    def edit_phone(self, phone, username):
        self._connection.execute(
            "UPDATE Members SET phone = ? WHERE username = ?", [phone, username])

    def edit_membership(self, memberhip, username):
        self._connection.execute(
            "UPDATE Members SET membership = ? WHERE username = ?", [memberhip, username])

    def make_admin(self, username):
        self._connection.execute(
            "UPDATE Members SET admin = 1 WHERE username = ?", [username])

    def unmake_admin(self, username):
        self._connection.execute(
            "UPDATE Members SET admin = 0 WHERE username = ?", [username])

    def get_all(self):
        return self._connection.execute(
            "SELECT * FROM Members").fetchall()

    def get_all_members(self):
        return self._connection.execute(
            '''SELECT username, name, membership FROM Members
            WHERE membership IS NOT NULL''').fetchall()

    def get_all_non_members(self):
        return self._connection.execute(
            "SELECT username, name FROM Members WHERE membership IS NULL").fetchall()

    def find_by_username(self, username):
        return self._connection.execute(
            "SELECT * FROM Members WHERE username = ?", [username]).fetchone()

    def find_info_by_username(self, username):
        return self._connection.execute(
            "SELECT username, name, email, phone, membership FROM Members WHERE username = ?",
            [username]).fetchone()

    def find_info_by_name(self, name):
        return self._connection.execute(
            "SELECT username, name, email, phone, membership FROM Members WHERE name = ?",
            [name]).fetchone()

    def delete_user(self, username):
        self._connection.execute(
            "DELETE FROM Members WHERE username = ?", [username])

    def delete_all(self):
        self._connection.execute("DELETE FROM Members")


register_repository = RegisterRepository(get_database_connection())
