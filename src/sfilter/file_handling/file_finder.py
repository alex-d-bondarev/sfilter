from pathlib import Path
from typing import Optional

from src.sfilter.file_handling.abstract_file_handler import AFileHandler
from src.sfilter.file_handling.existing_file import ExistingFile
from src.sfilter.file_handling.non_existing_file import NonExistingFile


def find_file(name: str, dir_path: Optional[str] = None) -> AFileHandler:
    """Find file by given name and return it in the form of FileHandlerInterface

    :param name:
    :param dir_path:
    :return:
    """
    try:
        if dir_path:
            return ExistingFile(Path(dir_path + name))
        else:
            return ExistingFile(next(Path(__file__).parent.parent.parent.parent.glob(name)))
    except StopIteration:
        return NonExistingFile(name)
