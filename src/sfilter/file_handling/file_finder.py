from pathlib import Path

from src.sfilter.file_handling.abstract_file_handler import AFileHandler
from src.sfilter.file_handling.existing_file import ExistingFile
from src.sfilter.file_handling.non_existing_file import NonExistingFile


def find_file(name: str) -> AFileHandler:
    """Find file by given name and return it in the form of FileHandlerInterface

    :param name:
    :return:
    """
    try:
        return ExistingFile(next(Path(__file__).parent.parent.parent.parent.glob(name)))
    except StopIteration:
        return NonExistingFile(name)
