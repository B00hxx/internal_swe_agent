from abc import ABC
from pathlib import Path
class Node(ABC):
    def __init__(self, path : Path, name : str):
        self.path = path
        self.name = name

    @property
    def is_folder(self):
        return False

    @property
    def is_file(self):
        return False