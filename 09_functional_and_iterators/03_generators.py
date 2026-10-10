"""03_generators.py - Produce values one at a time with yield."""


def countdown(start: int):
    while start > 0:
        yield start        # pause here and hand back a value
        start -= 1


def squares_up_to(limit: int):
    n = 1
    while n * n <= limit:
        yield n * n
        n += 1


print("Countdown:", list(countdown(5)))
print("Squares up to 50:", list(squares_up_to(50)))

# Generators are lazy: values are made only when needed
gen = countdown(3)
print(next(gen))
print(next(gen))
print(next(gen))

# A generator expression looks like a list comprehension with ( )
total = sum(n * n for n in range(1_000_000))
print("Sum of a million squares:", total)
