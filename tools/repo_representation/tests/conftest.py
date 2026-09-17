# tools/repo_representation/tests/conftest.py
import pytest
from pathlib import Path

@pytest.fixture
def dummy_project(tmp_path: Path) -> Path:
    base = tmp_path / "project"
    (base / "src").mkdir(parents=True)
    (base / "data").mkdir()
    (base / "main.py").write_text("")
    (base / "README.md").write_text("")
    (base / "src" / "utils.py").write_text("")
    return base