"""09_assertions_and_debugging.py - Catch bugs early with assert."""


def average(numbers: list) -> float:
    assert numbers, "list must not be empty"
    assert all(isinstance(n, (int, float)) for n in numbers), "all items must be numbers"
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))

try:
    average([])
except AssertionError as error:
    print("Caught:", error)

# assert is for developer mistakes, not user input
# Prefer raise ValueError for things users can cause

def positive_only(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    return n

print(positive_only(5))
