from abc import ABC, abstractmethod
from pathlib import Path
class Node(ABC):
    def __init__(self, path : Path,  root : Path | None = None):
        self.path = path
        self.root = root
        self.relative_path = self.path.relative_to(self.root) if self.root is not None else self.path 
        self.name = self.path.name

    @abstractmethod
    def serialize(self) -> dict:
        pass

    @property
    def is_folder(self) -> bool:
        return False

    @property
    def is_file(self) -> bool:
        return False
