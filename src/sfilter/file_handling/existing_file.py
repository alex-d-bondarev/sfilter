from pathlib import Path

from src.sfilter.file_handling import non_existing_file
from src.sfilter.file_handling.abstract_file_handler import \
    AFileHandler


class ExistingFile(AFileHandler):
    """Implement methods for existing file"""

    def __init__(self, path: Path):
        self.path_to_file = path

    def delete(self) -> AFileHandler:
        """Self evident"""
        self.path_to_file.unlink(missing_ok=True)
        return non_existing_file.NonExistingFile(self.path_to_file.name)

    def exists(self) -> bool:
        return True

    def get_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        return self.path_to_file.read_text()

    def name(self) -> str:
        """Return filename"""
        return self.path_to_file.name

    def write(self, text: str) -> AFileHandler:
        """Overwrite file content with the given text
        :param text:
        """
        self.path_to_file.write_text(text)
        return self
