from repositories.register_repository import (register_repository as default_register_repository)


class RegisterService:
    def __init__(self, register_repository = default_register_repository):
        self._register_repository = register_repository

    
    def create_user(self, username, password):
        if len(password) >= 8:
            existing_user = self._register_repository.find_by_username(username)
            if existing_user:
                print(f"Käyttäjätunnus {username} on jo käytössä")
            else:
                self._register_repository.create_user(username, password, None, None, None, None, 0)
        else:
            print("Salasanan tulee olla vähintään 8 merkkiä pitkä")


    def login(self, username, password):
        user = self._register_repository.find_by_username(username)
        if not user or user[1] != password:
            print("Väärä käyttäjätunnus tai salasana")
        else: 
            print("onnistui")

    def print_users(self):
        print(self._register_repository.get_all())



register_service = RegisterService()