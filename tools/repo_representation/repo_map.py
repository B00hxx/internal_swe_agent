from .node import Node
from .file_node import FileNode
from .folder_node import FolderNode
from pathlib import Path

class RepoMap:
    def __init__(self, root : Path):
        self.root = root
        self.tree : FolderNode = self._create_tree()

    def _create_tree(self) -> FolderNode:
        return FolderNode(path=self.root)

    def find_node(self, path : Path) -> Node | None:
        return self.tree.find_node(path=path)