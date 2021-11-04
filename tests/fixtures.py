import os
import pathlib

import pytest  # noqa


@pytest.fixture
def create_temp_file(request):
    """Create temporary test file"""
    path_to_file = os.path.join(
        pathlib.Path(__file__).parent.resolve(), request.param["file_name"]
    )
    file = open(path_to_file, "w")
    file.truncate(0)
    file.write(request.param["file_content"])
    file.close()

    yield path_to_file

    os.remove(path_to_file)
