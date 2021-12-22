import os
from pathlib import Path
from typing import TextIO

from src.sfilter.file_handling import non_existing_file
from src.sfilter.file_handling.abstract_file_handler import AFileHandler


class ExistingFile(AFileHandler):
    """Implement methods for existing file"""

    def __init__(self, path: Path):
        self.path_to_file = path
        if not Path(self.path_to_file).exists():
            raise FileNotFoundError

    def delete(self) -> AFileHandler:
        """Self evident"""
        self.path_to_file.unlink(missing_ok=True)
        return non_existing_file.NonExistingFile(self.path_to_file.name)

    def exists(self) -> bool:
        """:return: True (it exists)"""
        return True

    def file_path(self) -> str:
        """Self evident"""
        return os.fspath(self.path_to_file.resolve())

    def get_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        return self.path_to_file.read_text()

    def name(self) -> str:
        """Return filename"""
        return self.path_to_file.name

    def writable_file(self) -> TextIO:
        """Object that allows to write to path_to_file"""
        return self.path_to_file.open("w")

    def write(self, text: str) -> AFileHandler:
        """Overwrite file content with the given text
        :param text:
        """
        self.path_to_file.write_text(text)
        return self
