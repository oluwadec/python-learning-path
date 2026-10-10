"""03_bubble_sort.py - Swap neighbours until the list is sorted."""


def bubble_sort(items: list) -> list:
    data = items.copy()           # keep the original list unchanged
    n = len(data)

    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:           # already sorted, stop early
            break
    return data


if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Before:", numbers)
    print("After :", bubble_sort(numbers))
