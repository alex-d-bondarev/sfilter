import configparser

from configupdater import ConfigUpdater

from src.sfilter.file_handling.file_finder import find_file


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
        self.c_updater.write(self.config_file.writable_file())
