import pytest  # noqa

from src.sfilter.tools.radon import run_radon
from src.sfilter.file_utils import FileUtils
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_radon.py",
    "file_content": "import os"
}], indirect=True)
def test_radon(create_temp_file):
    """Test that radon is launched"""
    expected_content = "{\"mi\": 100.0, \"rank\": \"A\"}"
    run_radon(create_temp_file)

    file_util = FileUtils("radon.log")
    actual_content = file_util.get_file_content()
    file_util.delete_file()

    assert expected_content in actual_content
