from .node import Node
from pathlib import Path

class FolderNode(Node):
    def __init__(self, path : Path, name : str):
        super().__init__(path=path, name = name)
        self.children = list(self.path.iterdir())

    @property
    def is_folder(self):
        return True