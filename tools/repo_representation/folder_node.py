from __future__ import annotations
from pathlib import Path
from typing import Iterator
from .node import Node
from .file_node import FileNode

class FolderNode(Node):
    def __init__(self, path : Path, root : Path | None = None, parent : FolderNode | None = None,):
        super().__init__(path=path, root = root)
        self.parent = parent
        self.children : list[Node] = self._populate_children()

    def _populate_children(self) -> list[Node]:
            all_paths = list(self.path.iterdir())
            children = [FolderNode(path=element,
                                   root = self.root, 
                                   parent=self) 
                        if element.is_dir() 
                        else FileNode(path=element, 
                                      parent=self, 
                                      root = self.root) 
                        for element in all_paths]
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

    def serialize(self) -> dict:
        representation = dict()
        elements = self.children
        for element in elements:
            if isinstance(element, FileNode):
                representation[element.name] = element.serialize()
            elif isinstance(element, FolderNode):
                representation[element.name] = {"type" : "folder",
                                                "path" : str(element.relative_path),
                                                "children" : element.serialize()}
        return representation

    @property
    def is_folder(self) -> bool:
        return True