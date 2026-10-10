"""01_fundamentals.py - Variables, types, and basic operations."""

# Numbers
age = 20
height = 1.75
print("Age:", age, "| Height:", height)

# Strings
name = "Ada"
greeting = "Hello, " + name + "!"
print(greeting)
print(f"{name} is {age} years old.")

# Booleans
is_student = True
has_passed = age >= 18
print("Student?", is_student, "| Adult?", has_passed)

# Type checking
print("Type of age:", type(age))
print("Type of name:", type(name))

# Simple math
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")  # floor division
print(f"{a} % {b} = {a % b}")   # remainder
print(f"{a} ** {b} = {a ** b}")  # power

# Input (commented so the file runs without waiting)
# user_name = input("What is your name? ")
# print("Nice to meet you,", user_name)
