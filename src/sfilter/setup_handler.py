import configparser
from pathlib import Path
from typing import Optional

from configupdater import ConfigUpdater

from src.sfilter.file_handling.file_finder import (find_file_by_path,
                                                   find_file_relative)

SECTION_NAME = "sfilter"
NEW_CONFIG_FILE = "[sfilter]\n# Goal is '0'\nflake8 = -1\n# Goal is '100'\nmi = -1\n"


class SetUpHandler:
    """Handle setup.cfg"""

    def __init__(self, path: Optional[str] = None):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self._load_config_file(path)
        self.c_updater = ConfigUpdater()
        self.c_updater.read(self.config_file.file_path())

    def _load_config_file(self, path):
        if path:
            wrapped_path = Path(path)
            if path.endswith(".py"):
                wrapped_path = wrapped_path.parent
            wrapped_path = wrapped_path / "setup.cfg"
            self.config_file = find_file_by_path(path=wrapped_path)
        else:
            self.config_file = find_file_relative("setup.cfg")

        if not self.config_file.exists():
            self.config_file = self.config_file.write(NEW_CONFIG_FILE)

    def has_section(self, section: str) -> bool:
        """
        :return: True if no properties found. Else False
        """
        return self.c_updater.has_section(section)

    def save(self):
        """Save all given values to setup.cfg"""
        self.c_updater.write(self.config_file.writable_file())

    def get(self, param: str) -> Optional[str]:
        """Get param from 'sfilter' section

        :param param:
        :return: param value or None
        """
        option = self.c_updater.get(
            section=SECTION_NAME,
            option=param,
            fallback=None,
        )
        if option is None:
            return None
        else:
            return option.value

    def set(self, param: str, value: str) -> None:
        """Set 'sfilter' param with given value

        :param param:
        :param value:
        """
        self.c_updater[SECTION_NAME][param].value = value
