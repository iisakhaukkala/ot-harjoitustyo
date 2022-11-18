class UI:
    def __init__(self):
        pass

    def guide(self):
        print("Komennot: ")
        print("0 lopetus")
        print("1 kirjaudu sisään")
        print("2 luo käyttäjä")

    def run(self):
        self.guide()
        while True:
            print("")
            command = input("Komento: ")
            if command == "0":
                break
            elif command == "1":
                print("Työn alla")
            elif command == "2":
                print("Työn alla")
            