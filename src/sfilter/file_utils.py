from pathlib import Path


class FileHelper(object):
    """File utilities"""

    def __init__(self, name: str):
        self.path_to_file = next(Path().parent.parent.glob(name))

    def get_file_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        return self.path_to_file.read_text()

    def delete_file(self):
        """Self evident"""
        self.path_to_file.unlink(missing_ok=True)
