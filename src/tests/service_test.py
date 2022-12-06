import unittest
from services.register_service import register_service
from services.register_service import TooShortUsernameError, TooShortPasswordError, UsernameExistsError, InvalidCreditentialsError, UserNotFoundError


class TestService(unittest.TestCase):
    def setUp(self):
        register_service.delete_all()

    def test_too_short_username(self):
        self.assertRaises(TooShortUsernameError,
                          lambda: register_service.create_user("ab", "abc"))

    def test_too_short_password(self):
        self.assertRaises(TooShortPasswordError,
                          lambda: register_service.create_user("abc", "abcd"))

    def test_existing_username(self):
        register_service.create_user("abc", "abcdefgh")

        self.assertRaises(
            UsernameExistsError, lambda: register_service.create_user("abc", "12345678"))

    def test_get_users(self):
        register_service.create_user("abc", "abcdefgh")

        self.assertEqual(register_service.get_users(), [
                         ("abc", "abcdefgh", None, None, None, None, 0)])
