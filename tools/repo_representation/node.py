from abc import ABC, abstractmethod
from pathlib import Path
class Node(ABC):
    def __init__(self, path : Path):
        self.path = path
        self.name = self.path.name

    @abstractmethod
    def serialize(self) -> dict:
        pass

    @property
    def is_folder(self, root : Path | None = None) -> bool:
        return False

    @property
    def is_file(self) -> bool:
        return False
