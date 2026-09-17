from pathlib import Path
from tools.repo_representation import RepoMap

def test_find_node_returns_matching_node(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    node = repo_map.find_node(dummy_project / "src" / "utils.py")
    assert node is not None and node.name == "utils.py"


def test_find_node_returns_none_for_missing_path(dummy_project, tmp_path):
    repo_map = RepoMap(root=dummy_project)
    assert repo_map.find_node(tmp_path / "nope.py") is None


def test_iter_files_yields_only_files(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    names = {f.name for f in repo_map.tree.iter_files()}
    assert names == {"main.py", "README.md", "utils.py"}


def test_iter_folders_yields_only_folders(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    names = {f.name for f in repo_map.tree.iter_folders()}
    assert names == {"src", "data"}


def test_is_file_is_folder_flags(dummy_project):
    repo_map = RepoMap(root=dummy_project)
    file_node = repo_map.find_node(dummy_project / "main.py")
    folder_node = repo_map.find_node(dummy_project / "src")
    assert file_node.is_file and not file_node.is_folder
    assert folder_node.is_folder and not folder_node.is_file