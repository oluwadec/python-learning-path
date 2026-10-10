"""06_quiz_engine.py - Mini project: a quiz that marks answers."""

QUESTIONS = [
    {"question": "What keyword defines a function?", "answer": "def"},
    {"question": "Which type holds True or False?", "answer": "bool"},
    {"question": "What does len([1, 2, 3]) return?", "answer": "3"},
    {"question": "Which symbol starts a comment?", "answer": "#"},
]


def mark_quiz(questions: list, given_answers: list) -> int:
    score = 0
    for q, given in zip(questions, given_answers):
        correct = given.strip().lower() == q["answer"].lower()
        score += correct                     # True counts as 1
        mark = "correct" if correct else f"wrong (answer: {q['answer']})"
        print(f"Q: {q['question']}\n   You said {given!r} -> {mark}")
    return score


def grade(score: int, total: int) -> str:
    percent = score / total * 100
    if percent >= 75:
        return "Great job!"
    if percent >= 50:
        return "Good effort"
    return "Keep practising"


if __name__ == "__main__":
    answers = ["def", "int", "3", "#"]       # pretend the player typed these
    final = mark_quiz(QUESTIONS, answers)
    print(f"\nScore: {final}/{len(QUESTIONS)} - {grade(final, len(QUESTIONS))}")
