"""01_list_comprehensions.py - Build lists in a single line."""

numbers = range(1, 11)

squares = [n ** 2 for n in numbers]
print("Squares:", squares)

odd_cubes = [n ** 3 for n in numbers if n % 2 == 1]
print("Odd cubes:", odd_cubes)

# Transform text
names = ["ada", "ben", "chi"]
print("Capitalised:", [name.capitalize() for name in names])

# if/else goes BEFORE the for
labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 6)]
print("Labels:", labels)

# Nested loop in one line
pairs = [(x, y) for x in range(1, 3) for y in "ab"]
print("Pairs:", pairs)

# Set and dictionary versions
print("Unique lengths:", {len(name) for name in ["aa", "bb", "ccc"]})
print("Name lengths:", {name: len(name) for name in names})
