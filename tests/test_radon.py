import os
import pathlib

import pytest  # noqa

from src.sfilter.main import run_radon
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_radon.py",
    "file_content": "import os"
}], indirect=True)
def test_radon(create_temp_file):
    """Test that radon is launched"""
    expected_content = "{\"mi\": 100.0, \"rank\": \"A\"}"

    run_radon(create_temp_file)

    actual_content = _get_flake8_log_content_and_clean_up()
    assert expected_content in actual_content


def _get_flake8_log_content_and_clean_up():
    path_to_flake8_log = _get_log_path()
    file_content = ""

    for line in open(path_to_flake8_log):
        file_content += line

    os.remove(path_to_flake8_log)

    return file_content


def _get_log_path():
    path = os.path.join(
        pathlib.Path(__file__).parent.resolve(), "radon.log"
    )
    if os.path.isfile(path):
        return path
    else:
        return os.path.join(
            pathlib.Path(__file__).parent.parent.resolve(), "radon.log"
        )
