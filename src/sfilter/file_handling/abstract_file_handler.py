from __future__ import annotations

from abc import ABC, abstractmethod


class AFileHandler(ABC):
    """Describe methods for file handling"""

    @abstractmethod
    def delete(self) -> AFileHandler:
        """Self evident"""
        pass

    @abstractmethod
    def exists(self) -> bool:
        """return True if file exists, else False"""
        pass

    @abstractmethod
    def get_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        pass

    @abstractmethod
    def name(self) -> str:
        """Return filename"""
        pass

    @abstractmethod
    def write(self, text: str) -> AFileHandler:
        """Write given text to file
        :param text:
        """
        pass
