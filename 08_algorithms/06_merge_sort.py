"""06_merge_sort.py - Split the list, sort the halves, then merge."""


def merge(left: list, right: list) -> list:
    """Combine two sorted lists into one sorted list."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(items: list) -> list:
    if len(items) <= 1:           # base case
        return items
    middle = len(items) // 2
    return merge(merge_sort(items[:middle]), merge_sort(items[middle:]))


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Before:", data)
    print("After :", merge_sort(data))
