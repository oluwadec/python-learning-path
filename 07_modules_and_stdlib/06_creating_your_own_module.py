"""06_creating_your_own_module.py - Write code you can import."""

# This file can be imported as a module from another script.
# Functions defined here become available after: import this_file_name

PI = 3.14159


def circle_area(radius: float) -> float:
    return PI * radius ** 2


def circle_circumference(radius: float) -> float:
    return 2 * PI * radius


if __name__ == "__main__":
    # Only runs when you execute this file directly
    print("Area of r=3:", circle_area(3))
    print("Circumference of r=3:", circle_circumference(3))
    print("This file is being run as the main program.")
else:
    print("This file was imported as a module.")
