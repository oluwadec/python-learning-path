"""02_tuples_and_unpacking.py - Tuples are lists that cannot change."""

point = (10, 20)
print("Point:", point)

# Unpacking: split a tuple into separate variables
x, y = point
print(f"x={x}, y={y}")


def min_max(values: list) -> tuple:
    """Functions can return a tuple to give back several results."""
    return min(values), max(values)


low, high = min_max([4, 9, 1, 7])
print("Low:", low, "| High:", high)

# Swap two variables without a temporary one
a, b = 1, 2
a, b = b, a
print("Swapped:", a, b)

# Tuples cannot be changed
try:
    point[0] = 99
except TypeError as error:
    print("Error:", error)
