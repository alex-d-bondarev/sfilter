import json

from src.sfilter.file_handling.file_finder import find_file
from src.sfilter.setup_handler import SetUpHandler


class QualityHandler:
    """Handle quality metrics"""

    def __init__(self):
        self.setup = SetUpHandler()
        self.init_flake8 = self.setup.get("flake8")
        self.init_mi = self.setup.get("mi")

    def compare_metrics(self):
        """Compare initial metrics with new metrics"""
        self._count_flake8_flags()
        self._calculate_mi_stats()
        self._compare_flake8()
        self._compare_mi()
        self._save_result()

    def _count_flake8_flags(self):
        last_line_does_not_count = 1
        flake8_content = find_file("flake8.txt").get_content()
        self.new_flake8 = len(flake8_content.split("\n")) - last_line_does_not_count

    def _calculate_mi_stats(self):
        radon_content = find_file("radon.json").get_content()
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
                f"but became {self.new_mi}"
                "You have made code less maintainable. "
                "Please check radon.json for details. "
                "Please improve maintainability back. "
                "Appreciate if you make it even better. "
            )

    def _save_result(self):
        self.setup.set("flake8", str(self.new_flake8))
        self.setup.set("mi", str(self.new_mi))
        self.setup.save()
