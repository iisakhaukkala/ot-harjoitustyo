from repositories.register_repository import register_repository


class TooShortUsernameError(Exception):
    pass


class TooShortPasswordError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class InvalidCreditentialsError(Exception):
    pass


class RegisterService:
    def __init__(self, register_repo):
        self._register_repository = register_repo
        self._user = None

    def create_user(self, username, password):
        if len(username) < 3:
            raise TooShortUsernameError

        if len(password) < 8:
            raise TooShortPasswordError

        existing_user = self._register_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError

        self._register_repository.create_user(
            username, password, None, None, None, None, 0)

    def login(self, username, password):
        user = self._register_repository.find_by_username(username)

        if not user or user[1] != password:
            raise InvalidCreditentialsError

        self._user = user
        return user

    def logout(self):
        self._user = None

    def get_user_info(self):
        pass

    def print_users(self):
        print(self._register_repository.get_all())

    def edit_name(self):
        pass

    def edit_email(self):
        pass

    def edit_phone(self):
        pass

    def edit_membership(self):
        pass

    def print_info(self):
        pass

    def edit_info(self):
        pass

    def find_by_username(self):
        pass

    def find_by_name(self):
        pass

    def get_all_members(self):
        pass

    def get_all_non_members(self):
        pass

    def delete_user(self):
        pass

    def delete_all(self):
        pass


register_service = RegisterService(register_repository)
