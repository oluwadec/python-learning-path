"""07_quick_sort.py - Pick a pivot and split the list around it."""


def quick_sort(items: list) -> list:
    if len(items) <= 1:
        return items

    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    bigger = [x for x in items if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(bigger)


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5, 7]
    print("Before:", data)
    print("After :", quick_sort(data))
