"""04_selection_sort.py - Pick the smallest item again and again."""


def selection_sort(items: list) -> list:
    data = items.copy()

    for start in range(len(data)):
        smallest = start
        for i in range(start + 1, len(data)):
            if data[i] < data[smallest]:
                smallest = i
        data[start], data[smallest] = data[smallest], data[start]
    return data


if __name__ == "__main__":
    print(selection_sort([29, 10, 14, 37, 13]))
    print(selection_sort(["pear", "apple", "fig", "banana"]))
