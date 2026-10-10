"""05_scope_and_globals.py - Local vs global names."""

counter = 0  # global


def increase() -> None:
    global counter
    counter += 1


def show_local() -> None:
    counter = 99  # local, does not change the global
    print("Inside function, counter =", counter)


increase()
increase()
print("Global counter:", counter)
show_local()
print("Global still:", counter)

# Closures: a function that remembers values from where it was created
def make_multiplier(factor: int):
    def multiply(n: int) -> int:
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print("Double 7:", double(7))
print("Triple 7:", triple(7))
