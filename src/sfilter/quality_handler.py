import json
from pathlib import Path

from src.sfilter.file_handling.file_finder import find_file_by_path
from src.sfilter.setup_handler import SetUpHandler


class QualityHandler:
    """Handle quality metrics"""

    def __init__(self, path: str):
        self.path = path
        self.config_is_in_root = False

    def compare_metrics(self):
        """Compare initial metrics with new metrics"""
        self._count_new_flake8_flags()
        self._calculate_new_mi_stats()
        self._load_previous_metrics()
        self._compare_flake8()
        self._compare_mi()
        self._save_result()

    def _load_previous_metrics(self):
        if self.config_is_in_root:
            self.setup = SetUpHandler()
        else:
            self.setup = SetUpHandler(path=self.path)
        self.init_flake8 = self._load_init_value("flake8")
        self.init_mi = self._load_init_value("mi")

    def _load_init_value(self, key: str):
        value = self.setup.get(key)
        if value == "-1":
            return None
        else:
            return value

    def _count_new_flake8_flags(self):
        last_line_does_not_count = 1
        flake8_content = self._load_content(file_name="flake8.txt")
        self.new_flake8 = len(flake8_content.split("\n")) - last_line_does_not_count

    def _load_content(self, file_name: str):
        wrapped_path = self._generate_file_path(file_name)
        flake8_content = find_file_by_path(wrapped_path).get_content()
        return flake8_content

    def _generate_file_path(self, file_name):
        wrapped_path = Path(self.path)
        self.config_is_in_root = False
        if self.path.endswith(".py"):
            wrapped_path = wrapped_path.parent
        wrapped_path = wrapped_path / file_name

        if wrapped_path.exists():
            return wrapped_path
        else:
            self.config_is_in_root = True
            path = Path(file_name)
            return path

    def _calculate_new_mi_stats(self):
        radon_content = self._load_content(file_name="radon.json")
        radon_dict = json.loads(radon_content)
        mi_scores = 0

        for stat in radon_dict.items():
            mi_scores += float(stat[1]["mi"])

        self.new_mi = mi_scores / len(radon_dict)

    def _compare_flake8(self):
        if self.init_flake8 is not None:
            assert int(self.init_flake8) >= self.new_flake8, (
                f"Flake8 score was {self.init_flake8} "
                f"but became {self.new_flake8}. "
                "You have introduced new pip8 errors. "
                "Please check flake8.txt for details. "
                "Please fix all new and maybe some old errors"
            )

    def _compare_mi(self):
        if self.init_mi is not None:
            assert float(self.init_mi) <= self.new_mi, (
                f"Radon maintainability index was {self.init_mi} "
                f"but became {self.new_mi}. "
                "You have made code less maintainable. "
                "Please check radon.json for details. "
                "Please improve maintainability back. "
                "Appreciate if you make it even better. "
            )

    def _save_result(self):
        self.setup.set("flake8", str(self.new_flake8))
        self.setup.set("mi", str(self.new_mi))
        self.setup.save()
