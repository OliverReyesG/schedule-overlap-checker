from abc import ABC

class FileParser(ABC):
    def __read_file(self, path):
        pass

    def parse(self, path):
        pass


class EmployeeScheduleParser(FileParser):

    def __init__(self):
        pass

    # Defined for future implementation
    def __read_file(self, path: str) -> str:
        pass

    # Defined for future implementation
    def parse(self, path: str) -> dict:
        pass