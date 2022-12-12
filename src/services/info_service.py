from repositories.info_repository import info_repository


class InfoService:
    def __init__(self, info_repo):
        self._info_repository = info_repo

    def edit_info(self, textlist):
        self._info_repository.edit_info(textlist)

    def return_info(self):
        return self._info_repository.return_info()


info_service = InfoService(info_repository)
