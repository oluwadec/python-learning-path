"""09_counter_and_defaultdict.py - Count items and auto-create keys."""

from collections import Counter, defaultdict

words = ["red", "blue", "red", "green", "blue", "red", "yellow"]
print("Counter:", Counter(words))
print("Most common 2:", Counter(words).most_common(2))

# defaultdict creates a default when a key is missing
scores = defaultdict(list)
scores["Ada"].append(90)
scores["Ada"].append(85)
scores["Ben"].append(70)
print("Scores:", dict(scores))

# Group by first letter
names = ["Ada", "Ben", "Chi", "Amy", "Bob"]
by_letter = defaultdict(list)
for name in names:
    by_letter[name[0]].append(name)
print("By letter:", dict(by_letter))
