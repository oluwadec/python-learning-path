"""10_validating_data.py - Check data before you use it."""


def validate_user(data: dict) -> list:
    """Return a list of problems found in the user dictionary."""
    problems = []
    if "name" not in data or not str(data["name"]).strip():
        problems.append("name is required")
    age = data.get("age")
    if not isinstance(age, int) or age < 0 or age > 120:
        problems.append("age must be an integer between 0 and 120")
    email = data.get("email", "")
    if "@" not in email or "." not in email.split("@")[-1]:
        problems.append("email looks invalid")
    return problems


samples = [
    {"name": "Ada", "age": 20, "email": "ada@example.com"},
    {"name": "", "age": -5, "email": "not-an-email"},
    {"age": 30, "email": "ben@school.edu"},
]

for user in samples:
    issues = validate_user(user)
    status = "OK" if not issues else "; ".join(issues)
    print(f"{user} -> {status}")
