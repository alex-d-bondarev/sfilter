from __future__ import annotations


class FileHandlerInterface:
    """Describe methods for file handling"""

    def get_file_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        pass

    def delete(self) -> FileHandlerInterface:
        """Self evident"""
        pass
