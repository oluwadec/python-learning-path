"""09_zip_enumerate_any_all.py - Built-in helpers for loops."""

names = ["Ada", "Ben", "Chi"]
scores = [92, 74, 85]

# zip walks through lists side by side
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Turn two lists into a dictionary
print("Dictionary:", dict(zip(names, scores)))

# enumerate gives the position as well
for rank, name in enumerate(sorted(names, reverse=True), start=1):
    print(rank, name)

# any = at least one is true; all = every one is true
print("Anyone above 90?", any(s > 90 for s in scores))
print("Everyone passed (>= 60)?", all(s >= 60 for s in scores))

# Unzip back into separate lists
pairs = [("a", 1), ("b", 2)]
letters, numbers = zip(*pairs)
print(letters, numbers)
