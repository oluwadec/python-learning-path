"""01_try_except_basics.py - Handle errors instead of crashing."""

# Without try/except this would stop the program
try:
    number = int("not a number")
except ValueError:
    print("That was not a valid integer.")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Catch any error (use sparingly)
try:
    open("no_such_file.txt")
except Exception as error:
    print("Something went wrong:", type(error).__name__, error)

print("Program continues after the errors.")
