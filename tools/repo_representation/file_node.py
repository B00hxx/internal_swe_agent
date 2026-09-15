from .node import Node
from .folder_node import FolderNode
from pathlib import Path
class FileNode(Node):
    def __init__(self, path : Path, parent : FolderNode):
        super().__init__(path=path)
        self.extension = self.path.stem
        self.parent = parent

    @property
    def is_file(self) -> bool:
        return True