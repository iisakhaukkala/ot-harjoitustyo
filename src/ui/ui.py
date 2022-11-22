from repositories.user_repository import create_user, get_users

class UI:
    def __init__(self):
        pass

    def guide(self):
        print("Komennot: ")
        print("0 lopetus")
        print("1 luo käyttäjä")
        print("2 tulosta käyttäjät")

    def run(self):
        self.guide()
        while True:
            print("")
            command = input("Komento: ")
            if command == "0":
                break
            elif command == "1":
                username = input("Käyttäjätunnus: ")
                password = input("Salasana: ")
                create_user(username, password)
            elif command == "2":
                users = get_users()
                print(users)
            