from repositories.register_repository import register_repository


class TooShortUsernameError(Exception):
    pass


class TooShortPasswordError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class InvalidCreditentialsError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class DeletingYourselfError(Exception):
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

    # def get_user_info(self):
    #    return (self._user[0], self._user[2], self._user[3], self._user[4], self._user[5])

    def get_users(self):
        return self._register_repository.get_all()

    def update_user(self):
        user = self._user[0]
        self._user = self._register_repository.find_by_username(user)

    def edit_name(self, name):
        self._register_repository.edit_name(name, self._user[0])
        self.update_user()

    def edit_email(self, email):
        self._register_repository.edit_email(email, self._user[0])
        self.update_user()

    def edit_phone(self, phone):
        self._register_repository.edit_phone(phone, self._user[0])
        self.update_user()

    def edit_membership(self, membership, username):
        user = self._register_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError

        self._register_repository.edit_membership(membership, username)
        self.update_user()

    def find_info_by_username(self, username):
        user = self._register_repository.find_info_by_username(username)

        if not user:
            raise UserNotFoundError

        return user

    def find_info_by_name(self, name):
        user = self._register_repository.find_by_name(name)

        if not user:
            raise UserNotFoundError

        if user[0] == self._user[0]:
            raise DeletingYourselfError

        return user

    def get_all_members(self):
        return self._register_repository.get_all_members()

    def get_all_non_members(self):
        return self._register_repository.get_all_non_members()

    def delete_user(self, username):
        user = self._register_repository.find_by_username(username)

        if not user:
            raise UserNotFoundError

        self._register_repository.delete_user(username)

    def delete_all(self):
        self._register_repository.delete_all()

    def make_admin(self):
        self._register_repository.make_admin(self._user[0])
        self.update_user()

    def unmake_admin(self):
        self._register_repository.unmake_admin(self._user[0])
        self.update_user()


register_service = RegisterService(register_repository)
