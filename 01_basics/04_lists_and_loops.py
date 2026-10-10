"""04_lists_and_loops.py - Create, change, and loop through lists."""

fruits = ["apple", "banana", "cherry"]

# Add and remove items
fruits.append("mango")
fruits.insert(1, "kiwi")
fruits.remove("banana")
print("Fruits:", fruits)

# Loop with the position (index) using enumerate
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")

# Sorting
numbers = [42, 7, 19, 3, 25]
print("Sorted:", sorted(numbers))
print("Largest:", max(numbers), "| Smallest:", min(numbers))

# List comprehension: a short way to build a new list
squares = [n * n for n in range(1, 6)]
print("Squares:", squares)

# Keep only the even numbers
evens = [n for n in range(1, 11) if n % 2 == 0]
print("Evens:", evens)
