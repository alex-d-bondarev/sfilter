import configparser
from typing import Optional

from configupdater import ConfigUpdater

from src.sfilter.file_handling.file_finder import find_file

SECTION_NAME = "sfilter"


class SetUpHandler:
    """Handle setup.cfg"""

    def __init__(self):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config_file = find_file("setup.cfg")

        self.c_updater = ConfigUpdater()
        self.c_updater.read(self.config_file.file_path())

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
