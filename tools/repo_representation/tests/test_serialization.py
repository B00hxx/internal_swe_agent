from pathlib import Path
from ...repo_representation import RepoMap
from utils import create_dummy_project


def test_serialization():
    create_dummy_project()
    repo_map = RepoMap(root = Path(r'tools\repo_representation\tests\project'))
    serialized = repo_map.serialize()
    assert serialized == {'project': {'data': {'type': 'folder', 'path': 'data', 'children': {}}, 'main.py': {'type': 'file', 'path': 'main.py', 'extension': '.py', 'size': 0}, 'README.md': {'type': 'file', 'path': 'README.md', 'extension': '.md', 'size': 0}, 'src': {'type': 'folder', 'path': 'src', 'children': {'utils.py': {'type': 'file', 'path': 'src\\utils.py', 'extension': '.py', 'size': 0}}}}}