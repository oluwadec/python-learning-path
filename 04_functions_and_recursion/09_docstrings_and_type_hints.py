"""09_docstrings_and_type_hints.py - Document and type your functions."""

from typing import List, Optional


def average(numbers: List[float]) -> float:
    """Return the arithmetic mean of a list of numbers.

    Args:
        numbers: A non-empty list of numbers.

    Returns:
        The average as a float.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)


def find_first(items: List[str], prefix: str) -> Optional[str]:
    """Return the first item that starts with prefix, or None."""
    for item in items:
        if item.startswith(prefix):
            return item
    return None


print(average([10, 20, 30]))
print(find_first(["apple", "banana", "apricot"], "ap"))
print(find_first(["x", "y"], "z"))
print(average.__doc__.splitlines()[0])
