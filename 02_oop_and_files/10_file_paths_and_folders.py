"""10_file_paths_and_folders.py - Create folders and find files with pathlib."""

import tempfile
from pathlib import Path


def create_project(root: Path) -> None:
    """Build a small folder structure with a few files."""
    (root / "docs").mkdir(parents=True, exist_ok=True)
    (root / "src").mkdir(exist_ok=True)
    (root / "README.txt").write_text("My project\n")
    (root / "src" / "main.py").write_text("print('hi')\n")
    (root / "src" / "utils.py").write_text("# helpers\n")
    (root / "docs" / "guide.txt").write_text("How to use it\n")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as folder:
        project = Path(folder) / "my_project"
        create_project(project)

        # Find every Python file, including inside sub-folders
        for file in sorted(project.rglob("*.py")):
            print("Found:", file.relative_to(project))

        # Get file details
        readme = project / "README.txt"
        print("Name:", readme.name, "| Extension:", readme.suffix, "| Size:", readme.stat().st_size, "bytes")
