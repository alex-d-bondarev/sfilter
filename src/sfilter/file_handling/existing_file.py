from pathlib import Path

from src.sfilter.file_handling.file_handler_interface import \
    FileHandlerInterface
from src.sfilter.file_handling.non_existing_file import NonExistingFile


class ExistingFile(FileHandlerInterface):
    """Implement methods for existing file"""

    def __init__(self, path: Path):
        self.path_to_file = path

    def get_file_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        return self.path_to_file.read_text()

    def delete(self) -> FileHandlerInterface:
        """Self evident"""
        self.path_to_file.unlink(missing_ok=True)
        return NonExistingFile()
