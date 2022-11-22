import unittest
from database_connection import get_database_connection
from repositories.user_repository import create_user, get_users

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
    

    def test_get_users(self):
        self.connection.execute("DELETE FROM Members")
        create_user("Mikko", "meikäinen")
        self.assertEqual(get_users(), [('Mikko',)])
        