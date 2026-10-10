"""06_dunder_methods_and_dataclass.py - Special methods and dataclasses."""

from dataclasses import dataclass


class Vector:
    """A 2D vector that supports + and printing."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


@dataclass
class Book:
    """A dataclass writes __init__, __repr__ and __eq__ for you."""

    title: str
    author: str
    pages: int = 100


if __name__ == "__main__":
    v = Vector(1, 2) + Vector(3, 4)
    print(v, "| equal to (4, 6)?", v == Vector(4, 6))

    book = Book("Python Basics", "A. Writer", 250)
    print(book)
