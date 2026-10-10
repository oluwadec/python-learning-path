"""05_insertion_sort.py - Sort the way you sort playing cards."""


def insertion_sort(items: list) -> list:
    data = items.copy()

    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        # Shift bigger items one place to the right
        while j >= 0 and data[j] > current:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
    return data


if __name__ == "__main__":
    print(insertion_sort([12, 11, 13, 5, 6]))
    print(insertion_sort([3, 2, 1]))
    print(insertion_sort([]))
