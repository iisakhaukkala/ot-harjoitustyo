from services.register_service import (register_service as defaul_register_servive)


class UI:
    def __init__(self, register_service = defaul_register_servive):
        self._register_service = register_service

    def guide(self):
        print("Komennot: ")
        print("0 lopetus")
        print("1 luo käyttäjä")
        print("2 tulosta käyttäjät")
        print("3 kirjaudu sisään")

    def run(self):
        self.guide()
        while True:
            print("")
            command = input("Komento: ")
            if command == "0":
                break
            elif command == "1":
                username = input("Käyttäjätunnus: ")
                password = input("Salasana (väh. 8 merkkiä): ")
                self._register_service.create_user(username, password)
            elif command == "2":
                self._register_service.print_users()
            elif command == "3":
                username = input("Käyttäjätunnus: ")
                password = input("Salasana: ")
                self._register_service.login(username, password)