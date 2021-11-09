from pathlib import Path

from src.sfilter.file_handling.existing_file import ExistingFile
from src.sfilter.file_handling.file_handler_interface import \
    FileHandlerInterface
from src.sfilter.file_handling.non_existing_file import NonExistingFile


def find_file(name: str) -> FileHandlerInterface:
    """Find file by given name and return it in the form of FileHandlerInterface

    :param name:
    :return:
    """
    try:
        return ExistingFile(next(Path().parent.parent.glob(name)))
    except StopIteration:
        return NonExistingFile(name)
