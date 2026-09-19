from .node import Node
from .file_node import FileNode
from .folder_node import FolderNode
from pathlib import Path

class RepoMap:
    def __init__(self, root : Path):
        self.tree : FolderNode = self._create_root(root=root)

    def _create_root(self, root : Path) -> FolderNode:
        return FolderNode(path=root, 
                          root = root)

    def find_node(self, path : Path) -> Node | None:
        return self.tree.find_node(path=path)

    def serialize(self) -> dict:
        return {self.tree.name : {"type": "folder",
                              "path": str(self.tree.relative_path),
                              "children": self.tree.serialize()}}