class User:
    def __init__(self, username, password, name, email, phone, membership, admin): # pylint: disable=too-many-arguments
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone
        self.membership = membership
        self.admin = admin
