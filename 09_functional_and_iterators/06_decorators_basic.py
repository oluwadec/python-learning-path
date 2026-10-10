"""06_decorators_basic.py - Add behaviour to a function without changing it."""

import functools


def shout(func):
    @functools.wraps(func)          # keeps the original name and docstring
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        return func(*args, **kwargs)
    return wrapper


@shout
def greet(name):
    """Return a greeting."""
    return f"hello, {name}"


@log_calls
def add(a, b):
    return a + b


print(greet("Ada"))
print("Name kept:", greet.__name__)
print("Sum:", add(3, 4))
