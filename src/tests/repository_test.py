import unittest
from repositories.register_repository import register_repository


class TestRegister(unittest.TestCase):
    def setUp(self):
        register_repository.delete_all()

    def test_get_all(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        self.assertEqual(register_repository.get_all(), [
                         ('matti', 'meikäläinen', None, None, None, None, 0)])

    def test_delete_all(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.delete_all()
        self.assertEqual(register_repository.get_all(), [])

    def test_find_by_username(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', None, None, None, None, 0))

    def test_edit_name(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.edit_name("Matti Meikäläinen", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', "Matti Meikäläinen", None, None, None, 0))

    def test_edit_email(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.edit_email("matti.meikalainen@email.com", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', None, "matti.meikalainen@email.com", None, None, 0))

    def test_edit_phone(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.edit_phone("040 1234567", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', None, None, "040 1234567", None, 0))

    def test_edit_membership(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.edit_membership("01.01.2023", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', None, None, None, "01.01.2023", 0))

    def test_make_admin(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.make_admin("matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', None, None, None, None, 1))

    def test_unmake_admin(self):
        register_repository.create_user(
            "matti", "meikäläinen", None, None, None, None, 0)
        register_repository.make_admin("matti")
        register_repository.unmake_admin("matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikäläinen', None, None, None, None, 0))
