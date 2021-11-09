import os
import pathlib


class FileUtils(object):
    """File utilities"""

    def __init__(self, name: str):
        self.file_name = name
        self.path_to_file = self._get_file_path()

    def _get_file_path(self) -> str:
        path = os.path.join(pathlib.Path().parent.resolve(), self.file_name)
        if os.path.isfile(path):
            return path
        else:
            path = os.path.join(pathlib.Path().parent.parent.resolve(), self.file_name)
            if os.path.isfile(path):
                return path
            else:
                raise FileNotFoundError(self.file_name)

    def get_file_content(self) -> str:
        """Get content of the file that was given in constructor
        :return: file content as text
        """
        file_content = ""

        for line in open(self.path_to_file):
            file_content += line

        return file_content

    def delete_file(self):
        """Self evident"""
        os.remove(self.path_to_file)