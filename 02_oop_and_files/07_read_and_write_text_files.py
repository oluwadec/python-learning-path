"""07_read_and_write_text_files.py - Save and load plain text."""

import tempfile
from pathlib import Path


def write_notes(path: Path, notes: list) -> None:
    # "w" creates the file (or overwrites it)
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


def append_note(path: Path, note: str) -> None:
    # "a" adds to the end of the file
    with open(path, "a", encoding="utf-8") as file:
        file.write(note + "\n")


def read_notes(path: Path) -> list:
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    # A temporary folder keeps this demo from leaving files behind
    with tempfile.TemporaryDirectory() as folder:
        notes_file = Path(folder) / "notes.txt"

        write_notes(notes_file, ["Buy milk", "Call mum"])
        append_note(notes_file, "Study Python")

        for number, note in enumerate(read_notes(notes_file), start=1):
            print(f"{number}. {note}")
