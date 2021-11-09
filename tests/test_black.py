import pytest  # noqa

from src.sfilter.file_handling.file_handler_interface import FileHandlerInterface
from src.sfilter.tools.black import run_black
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_black.py",
    "file_content": "\nimport os"
}], indirect=True)
def test_black(create_temp_file: FileHandlerInterface):
    """Test that black is launched"""
    expected = "import os\n"

    run_black(create_temp_file.name())
    actual = create_temp_file.get_content()

    assert actual == expected
