"""02_multiple_exceptions.py - Respond differently to different errors."""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both values must be numbers"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "two"))

# One block can catch several exception types
values = ["10", "0", "hello"]
for text in values:
    try:
        n = int(text)
        print(100 / n)
    except (ValueError, ZeroDivisionError) as error:
        print(f"Problem with {text!r}: {error}")
