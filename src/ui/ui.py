from services.register_service import register_service, TooShortUsernameError, TooShortPasswordError, UsernameExistsError, InvalidCreditentialsError


class UI:
    def __init__(self, register_service=register_service):
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
                while True:
                    print("")
                    print("Peruuta syöttämällä kenttään 0")
                    username = input("Käyttäjätunnus (väh. 3 merkkiä): ")
                    if username == "0":
                        print("")
                        self.guide()
                        break
                    password = input("Salasana (väh. 8 merkkiä): ")
                    if password == "0":
                        print("")
                        self.guide()
                        break
                    try:
                        self._register_service.create_user(username, password)
                        print("Käyttäjätunnuksen luonti onnistui!")
                        break
                    except TooShortUsernameError:
                        print(
                            "Käyttäjätunnuksen tulee olla vähintään 3 merkkiä pitkä")
                    except TooShortPasswordError:
                        print("Salasanan tulee olla vähintään 8 merkkiä pitkä")
                    except UsernameExistsError:
                        print(f"Käyttäjätunnus {username} on jo käytössä")
            elif command == "2":
                self._register_service.print_users()
            elif command == "3":
                while True:
                    print("")
                    print("Peruuta syöttämällä kenttään 0")
                    username = input("Käyttäjätunnus: ")
                    if username == "0":
                        print("")
                        self.guide()
                        break
                    password = input("Salasana: ")
                    if password == "0":
                        print("")
                        self.guide()
                        break
                    try:
                        self._register_service.login(username, password)
                        print("Sisäänkirjautuminen onnistui!")
                        break
                    except InvalidCreditentialsError:
                        print("Käyttäjätunnus ja salasana eivät täsmää")
