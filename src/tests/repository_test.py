import unittest
from repositories.register_repository import register_repository


class TestRegister(unittest.TestCase):
    def setUp(self):
        register_repository.delete_all()

    def test_get_all(self):
        register_repository.create_user("Matti", "meikäläinen", None, None, None, None, 0)
        self.assertEqual(register_repository.get_all(), [('Matti', 'meikäläinen', None, None, None, None, 0)])

    def test_delete_all(self):
        register_repository.create_user("Matti", "meikäläinen", None, None, None, None, 0)
        register_repository.delete_all()
        self.assertEqual(register_repository.get_all(), [])

    def test_find_by_username(self):
        register_repository.create_user("Matti", "meikäläinen", None, None, None, None, 0)
        self.assertEqual(register_repository.find_by_username("Matti"), ('Matti', 'meikäläinen', None, None, None, None, 0))
