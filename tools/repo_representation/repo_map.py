from .node import Node
from .file_node import FileNode
from .folder_node import FolderNode
from pathlib import Path

class RepoMap:
    def __init__(self, root : Path):
        self.root = root
        self.tree : FolderNode = self._create_root()

    def _create_root(self) -> FolderNode:
        return FolderNode(path=self.root)

    def find_node(self, path : Path) -> Node | None:
        return self.tree.find_node(path=path)

    def build_tree(self):
        files, folders = self.tree.iter_files(), self.tree.iter_folders()
        for file in files:
            print(file.path)
        for folder in folders:
            print(folder)
        return
    