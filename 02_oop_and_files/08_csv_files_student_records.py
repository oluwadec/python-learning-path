"""08_csv_files_student_records.py - Work with spreadsheet-style CSV files."""

import csv
import tempfile
from pathlib import Path

students = [
    {"name": "Ada", "score": 92},
    {"name": "Ben", "score": 78},
    {"name": "Chi", "score": 85},
]


def save_students(path: Path, rows: list) -> None:
    # newline="" stops blank lines appearing on Windows
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(rows)


def load_students(path: Path) -> list:
    with open(path, newline="", encoding="utf-8") as file:
        return [{"name": r["name"], "score": int(r["score"])} for r in csv.DictReader(file)]


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as folder:
        csv_path = Path(folder) / "students.csv"
        save_students(csv_path, students)
        loaded = load_students(csv_path)

        average = sum(s["score"] for s in loaded) / len(loaded)
        print(f"Loaded {len(loaded)} students, average score {average:.1f}")
        best = max(loaded, key=lambda s: s["score"])
        print("Top student:", best["name"])
