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
                pass
            elif command == "2":
                pass