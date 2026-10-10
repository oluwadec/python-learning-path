"""02_default_and_keyword_args.py - Defaults and named arguments."""


def power(base: float, exponent: float = 2) -> float:
    return base ** exponent


def introduce(name: str, age: int = 18, city: str = "Lagos") -> str:
    return f"{name}, {age}, from {city}"


print(power(3))          # uses default exponent 2
print(power(3, 3))
print(power(base=2, exponent=10))

print(introduce("Ada"))
print(introduce("Ben", city="Abuja"))
print(introduce(age=25, name="Chi", city="Ibadan"))
