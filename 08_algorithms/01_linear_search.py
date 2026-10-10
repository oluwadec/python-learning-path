"""01_linear_search.py - Check items one by one."""


def linear_search(items: list, target) -> int:
    """Return the position of target, or -1 if it is not there."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def find_all(items: list, target) -> list:
    return [i for i, item in enumerate(items) if item == target]


if __name__ == "__main__":
    data = [4, 8, 15, 16, 23, 42, 8]
    print("Position of 23:", linear_search(data, 23))
    print("Position of 99:", linear_search(data, 99))
    print("All positions of 8:", find_all(data, 8))
