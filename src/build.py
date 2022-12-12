from initialize_database import initialize_database
from config import INFO_FILE_PATH


def build():
    initialize_database()
    with open(INFO_FILE_PATH, "w", encoding="utf-8") as file:
        file.write("Ohjeet puuttuvat")


if __name__ == "__main__":
    build()
