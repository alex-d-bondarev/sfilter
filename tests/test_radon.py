import pytest  # noqa

from src.sfilter.tools.radon import run_radon
from tests.file_utils import FileTestUtils
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_radon.py",
    "file_content": "import os"
}], indirect=True)
def test_radon(create_temp_file):
    """Test that radon is launched"""
    expected_content = "{\"mi\": 100.0, \"rank\": \"A\"}"
    file_util = FileTestUtils("radon.log")

    run_radon(create_temp_file)
    actual_content = file_util.get_file_content()
    file_util.delete_file()

    assert expected_content in actual_content
