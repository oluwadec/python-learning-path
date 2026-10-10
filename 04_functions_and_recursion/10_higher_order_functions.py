"""10_higher_order_functions.py - Functions that take or return functions."""


def apply_twice(func, value):
    return func(func(value))


def make_adder(n: int):
    def adder(x: int) -> int:
        return x + n
    return adder


def sort_by_length(words: list) -> list:
    return sorted(words, key=len)


print(apply_twice(lambda x: x + 1, 5))
add5 = make_adder(5)
print(add5(10))
print(sort_by_length(["fig", "banana", "kiwi", "apple"]))

# map and filter are higher-order functions
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda n: n ** 2, numbers)))
print(list(filter(lambda n: n % 2 == 0, numbers)))
