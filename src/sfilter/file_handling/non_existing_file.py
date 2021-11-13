from pathlib import Path

from src.sfilter.file_handling import existing_file
from src.sfilter.file_handling.abstract_file_handler import \
    AFileHandler


class NonExistingFile(AFileHandler):
    """Simplify delete flow"""

    def __init__(self, name):
        self.name = name

    def get_content(self) -> str:
        """This file does not exist. Raise exception"""
        raise FileNotFoundError(self.name)

    def name(self) -> str:
        """Return filename"""
        return self.name

    def write(self, text: str) -> AFileHandler:
        """Create new file and write given text to it
        :param text:
        """
        new_file = Path(self.name)
        new_file.touch()
        new_file.write_text(text)
        return existing_file.ExistingFile(new_file)

    def delete(self) -> AFileHandler:
        """Return self as already deleted/non-existing file"""
        return self
