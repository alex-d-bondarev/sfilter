"""
Use the same approach as in isort tests
https://github.com/PyCQA/isort/blob/main/tests/unit/test_main.py#L86
"""
import logging

from isort import main


def run_isort(dir_path: str) -> None:
    logging.info("Start isort execution")
    main.main([dir_path])
    logging.info("Finish isort execution")
