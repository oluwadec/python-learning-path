"""01_lists_deep_dive.py - Useful list operations."""

numbers = [5, 3, 8, 1, 9, 2]

print("Length:", len(numbers))
print("Slice [1:4]:", numbers[1:4])
print("Every 2nd item:", numbers[::2])

numbers.sort()                 # sorts the list itself
print("Sorted in place:", numbers)

numbers.reverse()
print("Reversed:", numbers)

last = numbers.pop()           # removes and returns the last item
print("Popped:", last, "| Left:", numbers)

# Joining two lists
combined = numbers + [100, 200]
print("Combined:", combined)

# Copying: a plain assignment does NOT copy
original = [1, 2, 3]
alias = original
real_copy = original.copy()
alias.append(4)
print("Original:", original, "| Copy:", real_copy)
