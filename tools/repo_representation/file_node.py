from __future__ import annotations
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .folder_node import FolderNode
from .node import Node
from pathlib import Path

class FileNode(Node):
    def __init__(self, path : Path, 
                 parent : FolderNode, 
                 root : Path | None = None):
        super().__init__(path=path, root=root)
        self.extension = self.path.suffix
        self.size = os.path.getsize(str(self.path))
        self.parent = parent

    def serialize(self) -> dict:
        info = {"type" : "file",
                        "path" : str(self.relative_path), 
                        "extension" : self.extension,
                        "size" : self.size}
        return info

    @property
    def is_file(self) -> bool:
        return True