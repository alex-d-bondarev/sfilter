import os

import pytest as pytest

from src.sfilter.main import run_black


@pytest.fixture
def file_to_check():
    """Create temporary test file"""
    test_file_name = "temp_file.py"
    path_to_file = os.path.join(os.path.curdir, test_file_name)
    file_content = """
    
    import os
    """
    file = open(path_to_file, "w")
    file.truncate(0)
    file.write(file_content)
    file.close()

    yield path_to_file

    os.remove(path_to_file)


def test_black(file_to_check):
    """Test black is launched"""
    expected = "import os"
    actual = ""
    run_black(file_to_check)

    for line in open(file_to_check):
        actual += line

    assert actual == expected
