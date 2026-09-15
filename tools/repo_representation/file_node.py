from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .folder_node import FolderNode
from .node import Node
from pathlib import Path

class FileNode(Node):
    def __init__(self, path : Path, parent : FolderNode):
        super().__init__(path=path)
        self.extension = self.path.suffix
        self.parent = parent

    @property
    def is_file(self) -> bool:
        return True