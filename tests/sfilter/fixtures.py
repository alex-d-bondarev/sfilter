import pytest  # noqa

from src.sfilter.file_handling.file_finder import find_file
from src.sfilter.file_handling.abstract_file_handler import AFileHandler


@pytest.fixture
def create_temp_file(request) -> AFileHandler:
    """Create temporary test file"""
    temp_file = find_file(
        request.param["file_name"]
    ).write(
        request.param["file_content"]
    )

    yield temp_file

    temp_file.delete()
