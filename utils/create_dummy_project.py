import inspect
from pathlib import Path


def create_dummy_project():
  caller_frame = inspect.stack()[1]
  caller_dir = Path(caller_frame.filename).resolve().parent
  base_dir = caller_dir / "project"
  src_dir = base_dir / "src"
  base_dir.mkdir(exist_ok=True)
  src_dir.mkdir(exist_ok=True)
  (base_dir / "main.py").touch(exist_ok=True)
  (base_dir / "README.md").touch(exist_ok=True)
  (src_dir / "utils.py").touch(exist_ok=True)
  print(f"Project structure created at: {base_dir}")