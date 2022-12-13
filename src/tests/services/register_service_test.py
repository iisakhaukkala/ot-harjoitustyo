import unittest
from services.register_service import register_service
from services.register_service import TooShortUsernameError, TooShortPasswordError, UsernameExistsError, InvalidCreditentialsError, UserNotFoundError, DeletingYourselfError


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

    def test_invalid_credidentials_username(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertRaises(InvalidCreditentialsError, lambda: register_service.login("acb", "abcdefgh"))

    def test_invalid_credidentials_password(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertRaises(InvalidCreditentialsError, lambda: register_service.login("abc", "12345678"))

    def test_login(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        self.assertEqual(register_service._user, ("abc", "abcdefgh", None, None, None, None, 0))
    
    def test_login_returns(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertEqual(register_service.login("abc", "abcdefgh"), ("abc", "abcdefgh", None, None, None, None, 0))

    def test_logout(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        register_service.logout()
        self.assertEqual(register_service._user, None)

    def test_edit_name(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        register_service.edit_name("Asd")
        self.assertEqual(register_service._user, ("abc", "abcdefgh", "Asd", None, None, None, 0))
    
    def test_edit_email(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        register_service.edit_email("asd@asd")
        self.assertEqual(register_service._user, ("abc", "abcdefgh", None, "asd@asd", None, None, 0))

    def test_edit_phone(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        register_service.edit_phone("123")
        self.assertEqual(register_service._user, ("abc", "abcdefgh", None, None, "123", None, 0))
    
    def test_edit_membership(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.edit_membership("01.01.2024", "abc")
        self.assertEqual(register_service.get_users(), [("abc", "abcdefgh", None, None, None, "01.01.2024",0)])

    def test_edit_membership_usernotfound(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertRaises(UserNotFoundError, lambda: register_service.edit_membership("01.01.2024", "asd"))

    def test_find_info_by_username(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertEqual(register_service.find_info_by_username("abc"), ("abc", None, None, None, None))

    def test_find_info_by_username_usernotfound(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertRaises(UserNotFoundError, lambda: register_service.find_info_by_username("asd"))

    def test_find_info_by_name(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.edit_name("Asd")
        self.assertEqual(register_service.find_info_by_name("Asd"), ("abc", "Asd", None, None, None))

    def test_find_info_by_name_usernotfound(self):
        register_service.create_user("abc", "abcdefgh")
        self.assertRaises(UserNotFoundError, lambda: register_service.find_info_by_name("Asd"))

    def test_get_all_members(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.edit_membership("01.01.2024", "abc")
        register_service.create_user("123", "12345678")
        self.assertEqual(register_service.get_all_members(), [("abc", None, "01.01.2024")])

    def test_get_all_non_members(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.edit_membership("01.01.2024", "abc")
        register_service.create_user("123", "12345678")
        self.assertEqual(register_service.get_all_non_members(), [("123", None)])

    def test_delete_user(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.create_user("123", "12345678")
        register_service.login("abc", "abcdefgh")
        register_service.delete_user("123")
        self.assertEqual(register_service.get_users(), [("abc", "abcdefgh", None, None, None, None, 0)])

    def test_delete_user_usernotfound(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        self.assertRaises(UserNotFoundError, lambda: register_service.delete_user("123"))

    def test_delete_user_deletingyourself(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        self.assertRaises(DeletingYourselfError, lambda: register_service.delete_user("abc"))

    def test_make_admin(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        register_service.make_admin()
        self.assertEqual(register_service._user, ("abc", "abcdefgh", None, None, None, None, 1))

    def test_unmake_admin(self):
        register_service.create_user("abc", "abcdefgh")
        register_service.login("abc", "abcdefgh")
        register_service.make_admin()
        register_service.unmake_admin()
        self.assertEqual(register_service._user, ("abc", "abcdefgh", None, None, None, None, 0))


    
