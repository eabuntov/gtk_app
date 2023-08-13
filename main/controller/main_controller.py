from ..model.main_model import MainModel


class MainController():

    @staticmethod
    def load_from_file() -> list:
        return [row for row in MainModel().csv_reader()]

    @staticmethod
    def load_from_api() -> list:
        return MainModel().fetch_apis()
