from .node import Node
from .file_node import FileNode
from pathlib import Path

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
        
    @property
    def is_folder(self) -> bool:
        return True