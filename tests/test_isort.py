import pytest  # noqa

from src.sfilter.tools.isort import run_isort
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_isort.py",
    "file_content": "import pathlib\nimport os"
}], indirect=True)
def test_isort(create_temp_file):
    """Test that isort is launched"""
    expected = "import os\nimport pathlib\n"
    actual = ""
    run_isort(create_temp_file)

    for line in open(create_temp_file):
        actual += line

    assert actual == expected
