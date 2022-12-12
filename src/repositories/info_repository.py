from config import INFO_FILE_PATH


class InfoRepository:
    def __init__(self, file_path):
        self._connection = file_path

    def edit_info(self, textlist):
        with open(self._connection, "w", encoding="utf-8") as file:
            for text in textlist:
                file.write(text)
                file.write("\n")

    def return_info(self):
        with open(self._connection, "r", encoding="utf-8") as file:
            contents = file.read()
        return contents


info_repository = InfoRepository(INFO_FILE_PATH)
