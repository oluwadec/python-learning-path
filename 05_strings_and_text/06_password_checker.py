"""06_password_checker.py - Rate how strong a password is."""


def check_password(password: str) -> tuple:
    """Return a score out of 5 and a list of tips."""
    tips = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        tips.append("use at least 8 characters")
    if any(ch.islower() for ch in password):
        score += 1
    else:
        tips.append("add a lowercase letter")
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        tips.append("add an uppercase letter")
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        tips.append("add a number")
    if any(not ch.isalnum() for ch in password):
        score += 1
    else:
        tips.append("add a symbol")

    return score, tips


if __name__ == "__main__":
    for pw in ["abc", "password1", "Str0ng!Pass"]:
        score, tips = check_password(pw)
        print(f"{pw!r}: {score}/5", "| tips:", ", ".join(tips) or "none")
