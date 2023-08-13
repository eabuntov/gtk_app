class MainController():
    @staticmethod
    def csv_reader():
        for row in open("test_assignment/База для тестового.csv", "r"):
            parsed = row.split(',')
            yield f"{parsed[1]} {parsed[3]}"
    @staticmethod
    def load_from_file() -> list:
        return [row for row in MainController.csv_reader()]
    @staticmethod
    def load_from_api() -> list:
        return [f"Example string {i}" for i in range(100)]