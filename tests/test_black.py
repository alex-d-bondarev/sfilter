import pytest  # noqa

from src.sfilter.tools.black import run_black
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_black.py",
    "file_content": "\nimport os"
}], indirect=True)
def test_black(create_temp_file):
    """Test that black is launched"""
    expected = "import os\n"
    actual = ""
    run_black(create_temp_file)

    for line in open(create_temp_file):
        actual += line

    assert actual == expected
