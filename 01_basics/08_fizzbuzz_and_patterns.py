"""08_fizzbuzz_and_patterns.py - Classic loop exercises."""


def fizzbuzz(limit: int) -> None:
    for n in range(1, limit + 1):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


def triangle(rows: int) -> None:
    """Print a triangle of stars."""
    for i in range(1, rows + 1):
        print("*" * i)


def multiplication_table(number: int) -> None:
    for i in range(1, 6):
        print(f"{number} x {i} = {number * i}")


if __name__ == "__main__":
    print("--- FizzBuzz ---")
    fizzbuzz(15)
    print("\n--- Triangle ---")
    triangle(5)
    print("\n--- Table of 7 ---")
    multiplication_table(7)
