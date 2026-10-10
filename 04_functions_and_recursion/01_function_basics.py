"""01_function_basics.py - Define and call functions."""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def describe_number(n: int) -> None:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


print(greet("Ada"))
print("5 + 3 =", add(5, 3))
describe_number(7)
describe_number(12)
