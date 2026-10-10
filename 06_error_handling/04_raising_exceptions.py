"""04_raising_exceptions.py - Create your own errors with raise."""


def set_age(age: int) -> None:
    if age < 0:
        raise ValueError("age cannot be negative")
    if age > 150:
        raise ValueError("age looks unrealistic")
    print(f"Age set to {age}")


for value in [25, -3, 200]:
    try:
        set_age(value)
    except ValueError as error:
        print("Rejected:", error)
