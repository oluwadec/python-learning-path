"""06_recursion_factorial.py - A function that calls itself."""


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:           # base case
        return 1
    return n * factorial(n - 1)  # recursive case


def countdown(n: int) -> None:
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)


print("5! =", factorial(5))
print("0! =", factorial(0))
countdown(3)
