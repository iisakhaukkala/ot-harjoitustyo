from services.register_service import register_service, TooShortUsernameError, TooShortPasswordError, UsernameExistsError, InvalidCreditentialsError, UserNotFoundError, DeletingYourselfError, InvalidDateError
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
        print("")

    def user_guide(self):
        print("")
        print(f"Kirjautuneena käyttäjänä {self._register_service._user[0]}")
        if self._register_service._user[5] == None:
            print("Jäsenyytesi ei ole voimassa")
        else:
            print(
                f"Jäsenyytesi voimassa {self._register_service._user[5]} asti")
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
        print(f"Kirjautuneena käyttäjänä {self._register_service._user[0]}")
        if self._register_service._user[5] == None:
            print("Jäsenyytesi ei ole voimassa")
        else:
            print(
                f"Jäsenyytesi voimassa {self._register_service._user[5]} asti")
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
        print("")

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
            name = input("Nimi: ")
            if name == "0":
                break
            try:
                self._register_service.create_user(username, password, name)
                print("Käyttäjätunnuksen luonti onnistui!")
                print("")
                break
            except TooShortUsernameError:
                print(
                    "Käyttäjätunnuksen tulee olla vähintään 3 merkkiä pitkä")
                print("")
            except TooShortPasswordError:
                print("Salasanan tulee olla vähintään 8 merkkiä pitkä")
                print("")
            except UsernameExistsError:
                print(f"Käyttäjätunnus {username} on jo käytössä")
                print("")

    def login(self):
        while True:
            print("")
            print("Kirjaudu sisään")
            print("Peruuta syöttämällä kenttään 0")
            print("")
            username = input("Käyttäjätunnus: ")
            if username == "0":
                print("")
                break
            password = input("Salasana: ")
            if password == "0":
                print("")
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
                print("")

    def edit_info_view(self):
        self.edit_info_guide()
        while True:
            command = input("Komento (komennolla k näet komennot): ")
            if command == "k" or command == "K":
                self.edit_info_guide()
            elif command == "0":
                if self._register_service._user[6] == 0:
                    self.user_guide()
                elif self._register_service._user[6] == 1:
                    self.admin_guide()
                break
            elif command == "1":
                self.user_info(register_service._user)
            elif command == "2":
                name = input("Nimi: ")
                self._register_service.edit_name(name)
                print("Nimen muokkaus onnistui!")
                print("")
            elif command == "3":
                email = input("Sähköposti: ")
                self._register_service.edit_email(email)
                print("Sähköpostin muokkaus onnistui!")
                print("")
            elif command == "4":
                phone = input("Puhelinnumero: ")
                self._register_service.edit_phone(phone)
                print("Puhelinnumeron muokkaus onnistui!")
                print("")

    def user_view(self):
        self.user_guide()
        while True:
            if register_service._user[6] == 1:
                register_service.logout()
                self.guide()
                break
            command = input("Komento (komennolla k näet komennot): ")
            if command == "k" or command == "K":
                self.user_guide()
            elif command == "0":
                register_service.logout()
                self.guide()
                break
            elif command == "1":
                self.edit_info_view()
            elif command == "2":
                print(self._info_service.return_info())
            elif command == "3":
                self.make_admin()

    def make_admin(self):
        while True:
            print("")
            sure = input("Oletko varma? y/n: ")
            if sure == "n" or sure == "N":
                break
            elif sure == "y" or sure == "Y":
                self._register_service.make_admin()
                print(
                    "Olet nyt admin, kirjaudu uudelleen saadaksesi admin-toiminnot käyttöön")
                break

    def admin_view(self):
        self.admin_guide()
        while True:
            if register_service._user[6] == 0:
                register_service.logout()
                self.guide()
                break
            command = input("Komento (komennolla k näet komennot): ")
            if command == "k" or command == "K":
                self.admin_guide()
            elif command == "0":
                register_service.logout()
                self.guide()
                break
            elif command == "1":
                self.edit_info_view()
            elif command == "2":
                print(self._info_service.return_info())
            elif command == "3":
                self.edit_instructions()
            elif command == "4":
                self.get_all_members()
            elif command == "5":
                self.get_all_non_members()
            elif command == "6":
                self.find_info_by_username()
            elif command == "7":
                self.find_info_by_name()
            elif command == "8":
                self.edit_membership()
            elif command == "9":
                self.delete_user()
            elif command == "10":
                self.unmake_admin()

    def edit_instructions(self):
        print("")
        print("Lopeta syöttämällä 0")
        textlist = []
        while True:
            text = input("")
            if text == "0":
                print("")
                break
            textlist.append(text)
        self._info_service.edit_info(textlist)

    def get_all_members(self):
        print("")
        members = self._register_service.get_all_members()
        print(f"Jäseniä on {len(members)}")
        for i in range(len(members)):
            print(f"{members[i][0]}, nimi: {members[i][1]}")
        print("")

    def get_all_non_members(self):
        print("")
        nonmembers = self._register_service.get_all_non_members()
        print(
            f"Käyttäjiä, jotka ei ole jäseniä on {len(nonmembers)}")
        print("Käyttäjät, jotka eivät ole jäseniä:")
        for i in range(len(nonmembers)):
            print(f"{nonmembers[i][0]}, nimi: {nonmembers[i][1]}")
        print("")

    def find_info_by_username(self):
        print("")
        username = input("Käyttäjätunnus: ")
        try:
            user = self._register_service.find_info_by_username(username)
            if user[4] == None:
                print(
                    f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys ei voimassa")
                print("")
            else:
                print(
                    f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys voimassa {user[4]} asti")
                print("")
        except UserNotFoundError:
            print(f"Käyttäjänimellä {username} ei löytynyt käyttäjää")
            print("")

    def find_info_by_name(self):
        print("")
        name = input("Nimi: ")
        try:
            user = self._register_service.find_info_by_name(name)
            if user[4] == None:
                print(
                    f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys ei voimassa")
                print("")
            else:
                print(
                    f"Käyttäjä {user[0]}, nimi {user[1]}, sähköposti {user[2]}, puhelin {user[3]}, jäsenyys voimassa {user[4]} asti")
                print("")
        except UserNotFoundError:
            print(f"Nimellä {name} ei löytynyt käyttäjää")
            print("")

    def edit_membership(self):
        print("")
        username = input(
            "Kenen jäsenyyttä haluat muokata (käyttäjätunnus)?: ")
        print(f"Mihin saakka käyttäjän {username} on voimassa?: ")

        try:
            year = int(input("Syötä vuosi: "))
            month = int(input("Syötä kuukausi: "))
            day = int(input("Syötä päivä: "))
            membership = str(year) + "-" + str(month) + "-" + str(day)
        except ValueError:
            print("Syötä vain lukuja")
            print("")
            return

        try:
            self._register_service.edit_membership(membership, username)
            print("Jäsenyyden muokkaus onnistui!")
            print("")
        except UserNotFoundError:
            print(f"Käyttäjänimellä {username} ei löytynyt käyttäjää")
            print("")
        except InvalidDateError:
            print(f"Päivämäärää {membership} ei ole olemassa")
            print("")

    def delete_user(self):
        print("")
        username = input("Käyttäjätunnus: ")
        while True:
            sure = input(
                f"Haluatko varmasti poistaa käyttäjän {username}? y/n: ")
            if sure == "n" or sure == "N":
                return
            elif sure == "y" or sure == "Y":
                try:
                    self._register_service.delete_user(username)
                    print(f"Käyttäjä {username} poistettu")
                    print("")
                    return
                except UserNotFoundError:
                    print(f"Käyttäjänimellä {username} ei löytynyt käyttäjää")
                    print("")
                    return
                except DeletingYourselfError:
                    print("Et voi poistaa itseäsi")
                    print("")
                    return

    def unmake_admin(self):
        print("")
        while True:
            sure = input("Oletko varma? y/n: ")
            if sure == "n" or sure == "N":
                break
            elif sure == "y" or sure == "Y":
                self._register_service.unmake_admin()
                print("Et ole enää admin")
                break

    def run(self):
        self.guide()
        while True:
            command = input("Komento (komennolla k näet komennot): ")
            if command == "k" or command == "K":
                self.guide()
            elif command == "0":
                break
            elif command == "1":
                self.create_user()
            elif command == "2":
                self.login()
