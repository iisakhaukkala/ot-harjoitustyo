import unittest
from repositories.register_repository import register_repository


class TestRegisterRepository(unittest.TestCase):
    def setUp(self):
        register_repository.delete_all()

    def test_get_all(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        self.assertEqual(register_repository.get_all(), [
                         ('matti', 'meikalainen', None, None, None, None, 0)])

    def test_delete_all(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.delete_all()
        self.assertEqual(register_repository.get_all(), [])

    def test_find_by_username(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', None, None, None, None, 0))

    def test_edit_name(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.edit_name("Matti Meikalainen", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', "Matti Meikalainen", None, None, None, 0))

    def test_edit_email(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.edit_email("matti.meikalainen@email.com", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', None, "matti.meikalainen@email.com", None, None, 0))

    def test_edit_phone(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.edit_phone("040 1234567", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', None, None, "040 1234567", None, 0))

    def test_edit_membership(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.edit_membership("01.01.2023", "matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', None, None, None, "01.01.2023", 0))

    def test_make_admin(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.make_admin("matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', None, None, None, None, 1))

    def test_unmake_admin(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.make_admin("matti")
        register_repository.unmake_admin("matti")
        self.assertEqual(register_repository.find_by_username(
            "matti"), ('matti', 'meikalainen', None, None, None, None, 0))

    def test_find_info_by_username(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        self.assertEqual(register_repository.find_info_by_username(
            "matti"), ('matti', None, None, None, None))

    def test_find_info_by_name(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.edit_name("Matti Meikalainen", "matti")
        self.assertEqual(register_repository.find_info_by_name(
            "Matti Meikalainen"), ('matti', "Matti Meikalainen", None, None, None))

    def test_get_all_members(self):
        register_repository.create_user(
            "matti", "meikalainen", "Matti Meikalainen", None, None, None, 0)
        register_repository.create_user(
            "erkki", "esimerkki", None, None, None, None, 0)
        register_repository.edit_membership("01.01.2023", "matti")
        self.assertEqual(register_repository.get_all_members(), [
                         ('matti', 'Matti Meikalainen', '01.01.2023')])

    def test_get_all_non_members(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.create_user(
            "erkki", "esimerkki", "Erkki Esimerkki", None, None, None, 0)
        register_repository.edit_membership("01.01.2023", "matti")
        self.assertEqual(register_repository.get_all_non_members(), [
                         ('erkki', 'Erkki Esimerkki')])

    def test_delete_user(self):
        register_repository.create_user(
            "matti", "meikalainen", None, None, None, None, 0)
        register_repository.create_user(
            "erkki", "esimerkki", None, None, None, None, 0)
        register_repository.delete_user("matti")
        self.assertEqual(register_repository.get_all(), [
                         ('erkki', 'esimerkki', None, None, None, None, 0)])
