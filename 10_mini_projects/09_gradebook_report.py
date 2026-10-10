"""09_gradebook_report.py - Mini project: a class report with rankings."""

students = {
    "Ada": {"math": 92, "english": 88, "science": 95},
    "Ben": {"math": 71, "english": 65, "science": 80},
    "Chi": {"math": 85, "english": 90, "science": 78},
    "Dayo": {"math": 55, "english": 62, "science": 58},
}


def letter(score: float) -> str:
    for cutoff, grade in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
        if score >= cutoff:
            return grade
    return "F"


def student_average(grades: dict) -> float:
    return sum(grades.values()) / len(grades)


def subject_average(subject: str) -> float:
    return sum(g[subject] for g in students.values()) / len(students)


if __name__ == "__main__":
    ranking = sorted(students, key=lambda n: student_average(students[n]), reverse=True)

    print(f"{'Rank':<5}{'Name':<8}{'Average':>8}  Grade")
    for rank, name in enumerate(ranking, start=1):
        avg = student_average(students[name])
        print(f"{rank:<5}{name:<8}{avg:>8.1f}  {letter(avg)}")

    print("\nSubject averages:")
    for subject in ["math", "english", "science"]:
        print(f"  {subject:<8}{subject_average(subject):.1f}")
