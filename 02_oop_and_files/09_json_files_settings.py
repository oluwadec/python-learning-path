"""09_json_files_settings.py - Store settings as JSON."""

import json
import tempfile
from pathlib import Path

DEFAULT_SETTINGS = {"theme": "dark", "font_size": 14, "languages": ["en"]}


def save_settings(path: Path, settings: dict) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=2)


def load_settings(path: Path) -> dict:
    """Return saved settings, or the defaults if the file is missing."""
    if not path.exists():
        return dict(DEFAULT_SETTINGS)
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as folder:
        settings_path = Path(folder) / "settings.json"

        print("Before saving:", load_settings(settings_path))

        settings = load_settings(settings_path)
        settings["theme"] = "light"
        settings["languages"].append("fr")
        save_settings(settings_path, settings)

        print("After saving: ", load_settings(settings_path))
