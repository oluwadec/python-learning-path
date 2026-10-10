"""03_sets_and_operations.py - Sets store unique items."""

# Duplicates disappear automatically
tags = {"python", "code", "python", "learn"}
print("Unique tags:", sorted(tags))

tags.add("fun")
tags.discard("code")
print("Updated:", sorted(tags))

class_a = {"Ada", "Ben", "Chi"}
class_b = {"Ben", "Dayo", "Chi", "Efe"}

print("In both:", sorted(class_a & class_b))
print("In either:", sorted(class_a | class_b))
print("Only in A:", sorted(class_a - class_b))
print("In one but not both:", sorted(class_a ^ class_b))

# A fast way to remove duplicates from a list
names = ["x", "y", "x", "z", "y"]
print("Without duplicates:", sorted(set(names)))
