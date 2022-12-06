from services.register_service import register_service, TooShortUsernameError, TooShortPasswordError, UsernameExistsError, InvalidCreditentialsError


class UI:
    def __init__(self, register_service=register_service):
        self._register_service = register_service

    def guide(self):
        print("")
        print("Komennot: ")
        print("0 lopetus")
        print("1 luo käyttäjä")
        print("2 kirjaudu sisään")
        print("3 tulosta kaikki")
        print("")

    def user_guide(self):
        print("")
        print(f"Kirjautuneena käyttäjänä {register_service._user[0]}")
        if register_service._user[5] == None:
            print("Jäsenyytesi ei ole voimassa")
        else:
            print(f"Jäsenyytesi voimassa {register_service._user[5]} asti")
        print("")
        print("Komennot:")
        print("0 kirjaudu ulos")
        print("1 tarkastele ja muokkaa tietojasi")
        print("2 tulosta jäsenyyden uusimisohjeet")
        print("3 hanki admin-oikeudet")
        print("")

    def edit_info_guide(self):
        print("")
        print("Komennot")
        print("0 takaisin")
        print("1 tarkastele tietojasi")
        print("2 muokkaa nimeä")
        print("3 muokkaa sähköpostiosoitetta")
        print("4 muokkaa puhelinnumeroa")
        print("")

    def admin_guide(self):
        print("")
        print(f"Kirjautuneena käyttäjänä {register_service._user[0]}")
        if register_service._user[5] == None:
            print("Jäsenyytesi ei ole voimassa")
        else:
            print(f"Jäsenyytesi voimassa {register_service._user[5]} asti")
        print("Olet admin")
        print("")
        print("Komennot:")
        print("0 kirjaudu ulos")
        print("1 tarkastele ja muokkaa tietojasi")
        print("2 tulosta jäsenyyden uusimisohjeet")
        print("3 muokkaa jäsenyyden uusimisohjeita")
        print("4 tulosta jäsenet")
        print("5 tulosta käyttäjät, jotka eivät ole jäseniä")
        print("6 etsi käyttäjä käyttäjänimellä")
        print("7 etsi käyttäjä nimellä")
        print("8 muokkaa jäsenyyksiä")
        print("9 poista käyttäjä")
        print("10 poista itseltäsi admin-oikeudet (kirjautuu ulos)")
        print("")

    def user_info(self, user):
        print("")
        print(f"Käyttäjän {user[0]} tiedot:")
        if user[2] == None:
            print("Nimeä ei löydy")
        else:
            print(f"Nimi: {user[2]}")
        if user[3] == None:
            print("Sähköpostia ei löydy")
        else:
            print(f"Sähköposti: {user[3]}")
        if user[4] == None:
            print("Puhelinnumeroa ei löydy")
        else:
            print(f"Puhelinnumero: {user[4]}")
        if user[5] == None:
            print("Jäsenyytesi ei ole voimassa")
        else:
            print(f"Jäsenyytesi voimassa {user[5]} asti")

    def create_user(self):
        while True:
            print("")
            print("Luo käyttäjä")
            print("Peruuta syöttämällä kenttään 0")
            print("")
            username = input("Käyttäjätunnus (väh. 3 merkkiä): ")
            if username == "0":
                break
            password = input("Salasana (väh. 8 merkkiä): ")
            if password == "0":
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

    def login(self):
        while True:
            print("")
            print("Kirjaudu sisään")
            print("Peruuta syöttämällä kenttään 0")
            print("")
            username = input("Käyttäjätunnus: ")
            if username == "0":
                break
            password = input("Salasana: ")
            if password == "0":
                break
            try:
                user = self._register_service.login(username, password)
                if user[6] == 0:
                    self.user_view()
                elif user[6] == 1:
                    self.admin_view()
                break
            except InvalidCreditentialsError:
                print("Käyttäjätunnus ja salasana eivät täsmää")

    def edit_info_view(self):
        while True:
            self.edit_info_guide()
            command = input("Komento: ")
            if command == "0":
                break
            elif command == "1":
                self.user_info(register_service._user)
            elif command == "2":
                name = input("Nimi: ")
                self._register_service.edit_name(name)
                print("Nimen muokkaus onnistui!")
            elif command == "3":
                email = input("Sähköposti: ")
                self._register_service.edit_email(email)
                print("Sähköpostin muokkaus onnistui!")
            elif command == "4":
                phone = input("Puhelinnumero: ")
                self._register_service.edit_phone(phone)
                print("Puhelinnumeron muokkaus onnistui!")

    def user_view(self):
        while True:
            if register_service._user[6] == 1:
                register_service.logout()
                break
            self.user_guide()
            command = input("Komento: ")
            if command == "0":
                register_service.logout()
                break
            elif command == "1":
                self.edit_info_view()
            elif command == "2":
                print("toimintoa ei vielä ole")  # tarkastele uusimisohjeita
            elif command == "3":
                while True:
                    print("")
                    sure = input("Oletko varma? y/n: ")
                    if sure == "n" or sure == "N":
                        break
                    elif sure == "y" or sure == "Y":
                        self._register_service.make_admin()
                        print("")
                        print(
                            "Olet nyt admin, kirjaudu uudelleen saadaksesi admin-toiminnot käyttöön")
                        break

    def admin_view(self):
        while True:
            if register_service._user[6] == 0:
                register_service.logout()
                break
            self.admin_guide()
            command = input("Komento: ")
            if command == "0":
                register_service.logout()
                break
            elif command == "1":
                self.edit_info_view()
            elif command == "2":
                print("toimintoa ei vielä ole")  # tarkastele uusimisohjeita
            elif command == "3":
                print("toimitoa ei vielä ole")  # muokkaa uusimisohjeita
            elif command == "4":
                # tulosta jäsenet ja niiden määrä
                print("toimitoa ei vielä ole")
            elif command == "5":
                # tulosta ei-jäsenet (ja niiden määrä)
                print("toimitoa ei vielä ole")
            elif command == "6":
                # etsi käyttäjää käyttäjänimellä
                print("toimitoa ei vielä ole")
            elif command == "7":
                print("toimitoa ei vielä ole")  # etsi käyttäjää nimellä
            elif command == "8":
                print("toimitoa ei vielä ole")  # muokkaa jäsenyyksiä
            elif command == "9":
                print("toimitoa ei vielä ole")  # poista käyttäjä
            elif command == "10":
                while True:
                    sure = input("Oletko varma? y/n: ")
                    if sure == "n" or sure == "N":
                        break
                    elif sure == "y" or sure == "Y":
                        print("lol")
                        self._register_service.unmake_admin()
                        print("")
                        print(
                            "Et ole enää admin")
                        break

    def run(self):
        while True:
            self.guide()
            command = input("Komento: ")
            if command == "0":
                break
            elif command == "1":
                self.create_user()
            elif command == "2":
                self.login()
            elif command == "3":
                print(self._register_service.get_users())
