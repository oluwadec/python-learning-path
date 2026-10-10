"""10_two_sum_and_max_subarray.py - Two popular interview-style problems."""


def two_sum(numbers: list, target: int):
    """Find two positions whose values add up to target."""
    seen = {}                       # value -> position
    for index, value in enumerate(numbers):
        needed = target - value
        if needed in seen:
            return seen[needed], index
        seen[value] = index
    return None


def max_subarray(numbers: list) -> int:
    """Largest sum of any run of neighbouring numbers (Kadane's algorithm)."""
    best = current = numbers[0]
    for value in numbers[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best


if __name__ == "__main__":
    print("Two sum:", two_sum([2, 7, 11, 15], 9))
    print("No match:", two_sum([1, 2, 3], 100))
    print("Best run:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
