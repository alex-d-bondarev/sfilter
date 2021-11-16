import json

from src.sfilter.file_handling.file_finder import find_file
from src.sfilter.setup_handler import SetUpHandler
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
    setup = SetUpHandler()
    new_number_of_flake8_flags = _count_flake8_flags()
    new_mi = _get_new_mi_stats()

    if setup.get("flake8") is not None:
        flake8_before = setup.get("flake8")
        assert int(flake8_before) >= new_number_of_flake8_flags, (
            f"Flake8 score was {flake8_before} "
            f"but became {new_number_of_flake8_flags}. "
            "You have introduced new pip8 errors. "
            "Please check flake8.txt for details. "
            "Please fix all new and maybe some old errors"
        )

    if setup.get("mi") is not None:
        mi_before = setup.get("mi")
        assert float(mi_before) <= new_mi, (
            f"Radon maintainability index was {mi_before} "
            f"but became {new_mi}"
            "You have made code less maintainable. "
            "Please check radon.json for details. "
            "Please improve maintainability back. "
            "Appreciate if you make it even better. "
        )

    setup.set("flake8", str(new_number_of_flake8_flags))
    setup.set("mi", str(new_mi))
    setup.save()

    assert True, "Good work!"


def _parse_properties_into_dict(before_dict, s_file):
    s_file_content = s_file.get_content()
    for line in s_file_content.split("\n"):
        if _is_property(line):
            k, v = line.rstrip().split("=")
            before_dict[k] = v


def _is_property(line):
    return line and not line.startswith("#")


def _count_flake8_flags() -> int:
    last_line_does_not_count = 1
    flake8_content = find_file("flake8.txt").get_content()
    return len(flake8_content.split("\n")) - last_line_does_not_count


def _get_new_mi_stats() -> float:
    radon_content = find_file("radon.json").get_content()
    radon_dict = json.loads(radon_content)
    mi_scores = 0

    for stat in radon_dict.items():
        mi_scores += float(stat[1]["mi"])

    return mi_scores / len(radon_dict)


def run_all(dir_path):
    clean_before_test()
    run_black(dir_path)
    run_isort(dir_path)
    run_flake8(dir_path)
    run_radon(dir_path)
    check_quality()
