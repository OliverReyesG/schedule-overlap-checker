from abc import ABC

class FileParser(ABC):
    def read_file(self, path):
        pass

    def parse(self):
        pass


class TextFileParser(FileParser):
    # Defined for future implementation
    def read_file(self, path: str) -> str:
        pass

    # Defined for future implementation
    def parse(self) -> dict:
        pass