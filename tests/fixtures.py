import pytest  # noqa

from src.sfilter.file_handling.file_finder import find_file
from src.sfilter.file_handling.file_handler_interface import FileHandlerInterface


@pytest.fixture
def create_temp_file(request) -> FileHandlerInterface:
    """Create temporary test file"""
    temp_file = find_file(request.param["file_name"])
    temp_file = temp_file.write(request.param["file_content"])

    yield temp_file

    temp_file.delete()
