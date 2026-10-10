"""07_decorators_with_arguments.py - Decorators that you can configure."""

import functools


def repeat(times: int):
    """A decorator factory: repeat(3) returns the real decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def validate_positive(func):
    @functools.wraps(func)
    def wrapper(number):
        if number <= 0:
            raise ValueError(f"{func.__name__} needs a positive number")
        return func(number)
    return wrapper


@repeat(times=3)
def cheer():
    print("Hooray!")


@validate_positive
def square_root(number):
    return number ** 0.5


cheer()
print("sqrt(16) =", square_root(16))
try:
    square_root(-4)
except ValueError as error:
    print("Error:", error)
