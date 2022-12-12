from services.register_service import register_service, TooShortUsernameError, TooShortPasswordError, UsernameExistsError, InvalidCreditentialsError, UserNotFoundError, DeletingYourselfError
from services.info_service import info_service


class UI:
    def __init__(self, register_service=register_service, info_service=info_service):
        self._register_service = register_service
        self._info_service = info_service

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
                print(self._info_service.return_info())
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
                print(self._info_service.return_info())
            elif command == "3":
                print("Lopeta syöttämällä 0")
                textlist = []
                while True:
                    text = input("")
                    if text == "0":
                        break
                    textlist.append(text)
                self._info_service.edit_info(textlist)
            elif command == "4":
                users = register_service.get_all_members()
                print(f"Jäseniä on {len(users)} kappaletta")
                for i in range(len(users)):
                    print(f"{users[i][0]}, nimi: {users[i][1]}")
            elif command == "5":
                nonusers = register_service.get_all_non_members()
                print(
                    f"Käyttäjiä, jotka ei ole jäseniä on {len(nonusers)} kappaletta")
                print("Käyttäjät, jotka eivät ole jäseniä:")
                for i in range(len(nonusers)):
                    print(f"{nonusers[i][0]}, nimi: {nonusers[i][1]}")
            elif command == "6":
                username = input("Käyttäjätunnus: ")
                try:
                    user = register_service.find_info_by_username(username)
                    if user[4] == None:
                        print(
                            f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys ei voimassa")
                    else:
                        print(
                            f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys voimassa {user[4]} asti")
                except UserNotFoundError:
                    print(f"Käyttäjänimellä {username} ei löytynyt käyttäjää")
            elif command == "7":
                name = input("Nimi: ")
                try:
                    user = register_service.find_info_by_name(name)
                    if user[4] == None:
                        print(
                            f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys ei voimassa")
                    else:
                        print(
                            f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys voimassa {user[4]} asti")
                except UserNotFoundError:
                    print(f"Nimellä {name} ei löytynyt käyttäjää")
            elif command == "8":
                username = input(
                    "Kenen jäsenyyttä haluat muokata (käyttäjätunnus)?: ")
                membership = input(
                    f"Mihin saakka käyttäjän {username} on voimassa?: ")
                try:
                    register_service.edit_membership(membership, username)
                    print("Jäsenyyden muokkaus onnistui!")
                except UserNotFoundError:
                    print(f"Käyttäjänimellä {username} ei löytynyt käyttäjää")
            elif command == "9":
                username = input("Käyttäjätunnus: ")
                sure = input(
                    f"Haluatko varmasti poistaa käyttäjän {username}? y/n")
                if sure == "n" or sure == "N":
                    break
                elif sure == "y" or sure == "Y":
                    try:
                        register_service.delete_user(username)
                        print(f"Käyttäjä {username} poistettu")
                    except UserNotFoundError:
                        print(
                            f"Käyttäjänimellä {username} ei löytynyt käyttäjää")
                    except DeletingYourselfError:
                        print(f"Et voi poistaa itseäsi")
            elif command == "10":
                while True:
                    sure = input("Oletko varma? y/n: ")
                    if sure == "n" or sure == "N":
                        break
                    elif sure == "y" or sure == "Y":
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
