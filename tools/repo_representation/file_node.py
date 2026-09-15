from .node import Node
from pathlib import Path

class FileNode(Node):
    def __init__(self, path : Path, name : str):
        super().__init__(path=path, name = name)
    @property
    def is_file(self):
        return True