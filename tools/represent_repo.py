from langchain_core.tools import tool
from pathlib import Path
from .repo_representation import RepoMap


@tool
def represent_repo(path : Path) -> dict:
    """
    This tool can be used to return a dictionary which contains the representation of the repo through a provided path
    it takes a parameter path (Path) and returns a dictionary
    """
    root = RepoMap(root = path)
    return root.serialize()

