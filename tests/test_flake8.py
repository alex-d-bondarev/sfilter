import os
import pathlib

import pytest  # noqa

from src.sfilter.tools.flake8 import run_flake8
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_flake8.py",
    "file_content": "\nimport os"
}], indirect=True)
def test_flake8(create_temp_file):
    """Test that flake8 is launched"""
    error1 = "F401 'os' imported but unused"
    error2 = "W292 no newline at end of file"

    run_flake8(create_temp_file)

    actual_content = _get_flake8_log_content_and_clean_up()
    assert error1 in actual_content
    assert error2 in actual_content


def _get_flake8_log_content_and_clean_up():
    path_to_flake8_log = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "flake8.log"
    )
    file_content = ""

    for line in open(path_to_flake8_log):
        file_content += line

    os.remove(path_to_flake8_log)

    return file_content
