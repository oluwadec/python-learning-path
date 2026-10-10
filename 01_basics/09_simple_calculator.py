"""09_simple_calculator.py - Small functions combined into a calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


# Map each symbol to its function
OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(a: float, symbol: str, b: float):
    if symbol not in OPERATIONS:
        return f"Error: unknown operator '{symbol}'"
    return OPERATIONS[symbol](a, b)


if __name__ == "__main__":
    tests = [(8, "+", 2), (8, "-", 2), (8, "*", 2), (8, "/", 2), (8, "/", 0), (8, "%", 2)]
    for a, symbol, b in tests:
        print(f"{a} {symbol} {b} = {calculate(a, symbol, b)}")
