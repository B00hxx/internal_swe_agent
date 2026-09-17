from pathlib import Path
from tools.repo_representation import RepoMap


def test_file_node_serialize(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    main_py = repo_map.serialize()["project"]["children"]["main.py"]
    assert main_py == {"type": "file", "path": "main.py", "extension": ".py", "size": 0}


def test_folder_node_serialize_nested(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    src = repo_map.serialize()["project"]["children"]["src"]
    assert src["type"] == "folder"
    assert src["path"] == "src"
    assert src["children"]["utils.py"]["path"] == str(Path("src") / "utils.py")


def test_serialize_empty_folder(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    data = repo_map.serialize()["project"]["children"]["data"]
    assert data == {"type": "folder", "path": "data", "children": {}}