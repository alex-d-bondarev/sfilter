from src.sfilter.file_handling.file_handler_interface import \
    FileHandlerInterface


class NonExistingFile(FileHandlerInterface):
    """Simplify delete flow"""

    def get_file_content(self) -> str:
        """This file does not exist. Raise exception"""
        raise FileNotFoundError()

    def delete(self) -> FileHandlerInterface:
        """Return self as already deleted/non-existing file"""
        return self
