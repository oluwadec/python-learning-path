"""03_args_and_kwargs.py - Variable numbers of arguments."""


def total(*numbers: float) -> float:
    return sum(numbers)


def show_profile(name: str, **details) -> None:
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"  {key}: {value}")


print("Total:", total(1, 2, 3, 4, 5))
print("Total of nothing:", total())

show_profile("Ada", age=20, course="Math", year=2)
