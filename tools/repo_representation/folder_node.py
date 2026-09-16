from __future__ import annotations
from pathlib import Path
from typing import Iterator
from .node import Node
from .file_node import FileNode

class FolderNode(Node):
    def __init__(self, path : Path, parent : FolderNode | None = None,):
        super().__init__(path=path)
        self.parent = parent
        self.children : list[Node] = self._populate_children()

    def _populate_children(self) -> list[Node]:
            all_paths = list(self.path.iterdir())
            children = [FolderNode(path=element, parent=self) if element.is_dir() else FileNode(path=element, parent=self) for element in all_paths]
            return children

    def find_node(self, path : Path) -> Node | None:
        elements = self.children
        for node in elements:
            if node.path == path:
                return node
            if isinstance(node, FolderNode):
                result = node.find_node(path = path)
                if result is not None:
                     return result
        return None

    def iter_folders(self) -> Iterator['FolderNode']:
        for node in self.children:
            if isinstance(node, FolderNode):
                yield node
                yield from node.iter_folders()

    def iter_files(self) -> Iterator['FileNode']:
        for node in self.children:
            if isinstance(node, FileNode):
                yield node
            elif isinstance(node, FolderNode):
                yield from node.iter_files()

    def build_tree(self):
        files, folders = self.iter_files(), self.iter_folders()
        for file in files:
            print(file.path)
        for folder in folders:
            print(folder)
        return
    
    @property
    def is_folder(self) -> bool:
        return True