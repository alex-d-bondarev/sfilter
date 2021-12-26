"""
Use the same approach as in flake8 tests
https://github.com/PyCQA/flake8/blob/main/tests/integration/test_main.py#L15
"""
import logging

from flake8.main import cli


def run_flake8(path: str) -> None:
    try:
        logging.info("Start flake8 execution")
        cli.main([path, "--output-file=flake8.txt"])
    except SystemExit:
        # expected exception
        logging.info("Finish flake8 execution")
