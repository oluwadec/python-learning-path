"""08_sorting_with_keys.py - Sort data in different ways."""

people = [
    {"name": "Ada", "age": 31},
    {"name": "Ben", "age": 25},
    {"name": "Chi", "age": 31},
    {"name": "Dayo", "age": 19},
]

# Sort by one field
by_age = sorted(people, key=lambda p: p["age"])
print("By age:", [p["name"] for p in by_age])

# Largest first
oldest_first = sorted(people, key=lambda p: p["age"], reverse=True)
print("Oldest first:", [p["name"] for p in oldest_first])

# Sort by age, then by name for ties
tie_break = sorted(people, key=lambda p: (-p["age"], p["name"]))
print("Age desc, then name:", [p["name"] for p in tie_break])

# Sort words by length
words = ["banana", "fig", "cherry", "kiwi"]
print("By length:", sorted(words, key=len))
