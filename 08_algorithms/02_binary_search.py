"""02_binary_search.py - Find items quickly in a SORTED list."""


def binary_search(items: list, target) -> int:
    low, high = 0, len(items) - 1

    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        elif items[middle] < target:
            low = middle + 1       # target must be in the right half
        else:
            high = middle - 1      # target must be in the left half

    return -1


if __name__ == "__main__":
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    for target in [23, 2, 91, 50]:
        print(f"Search {target}: index {binary_search(sorted_numbers, target)}")
