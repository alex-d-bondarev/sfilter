import json
import os

from src.sfilter.file_handling.file_finder import find_file
from src.sfilter.tools.black import run_black
from src.sfilter.tools.flake8 import run_flake8
from src.sfilter.tools.isort import run_isort
from src.sfilter.tools.radon import run_radon


def clean_before_test() -> None:
    """Clean up analysis logs before tests"""
    find_file("flake8.txt").delete()
    find_file("radon.json").delete()


def check_quality():
    """Analyse code quality"""
    before = _read_before_dict()
    new_flake8 = _get_new_flake8_stats()
    new_mi = _get_new_mi_stats()

    if len(before) != 0:
        assert int(before["flake8"]) >= new_flake8, (
            f"Flake8 score was {before['flake8']} "
            f"but became {new_flake8}. "
            "You have introduced new pip8 errors. "
            "Please check flake8.txt for details. "
            "Please fix all new and maybe some old errors"
        )
        assert float(before["mi"]) <= new_mi, (
            f"Radon maintainability index was {before['mi']} "
            f"but became {new_mi}"
            "You have made code less maintainable. "
            "Please check radon.json for details. "
            "Please improve maintainability back. "
            "Appreciate if you make it even better. "
        )

    _save_new_results(new_flake8, new_mi)

    assert True, "Good work!"


def _read_before_dict():
    before_dict = dict()
    root_dir = os.path.dirname(os.curdir)
    project_quality = os.path.join(root_dir, "./sfilter.txt")

    if os.path.exists(project_quality):
        for line in open(project_quality):
            if not line.startswith("#"):
                k, v = line.rstrip().split("=")
                before_dict[k] = v

    return before_dict


def _get_new_flake8_stats():
    root_dir = os.path.dirname(os.curdir)
    flake8_log = os.path.join(root_dir, "./flake8.txt")
    return len(open(flake8_log).readlines())


def _get_new_mi_stats():
    root_dir = os.path.dirname(os.curdir)
    radon_log = os.path.join(root_dir, "./radon.json")
    radon_log_file = open(radon_log)
    radon_dict = json.load(radon_log_file)
    mi_scores = 0

    for stat in radon_dict.items():
        mi_scores += float(stat[1]["mi"])

    return mi_scores / len(radon_dict)


def _save_new_results(new_flake8, new_mi):
    root_dir = os.path.dirname(os.curdir)
    project_quality = os.path.join(root_dir, "./sfilter.txt")
    file = open(project_quality, "w")
    file.truncate(0)
    file.write(f"# Goal is '0'\nflake8={new_flake8}\n")
    file.write(f"# Goal is '100'\nmi={new_mi}\n")


def run_all(dir_path):
    clean_before_test()
    run_black(dir_path)
    run_isort(dir_path)
    run_flake8(dir_path)
    run_radon(dir_path)
    check_quality()
