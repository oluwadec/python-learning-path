"""03_inheritance_shapes.py - Child classes reuse a parent class."""

import math


class Shape:
    """Parent class: every shape has a name and an area."""

    def __init__(self, name: str):
        self.name = name

    def area(self) -> float:
        return 0.0

    def describe(self) -> str:
        return f"{self.name} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")  # call the parent's __init__
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 2)]
    for shape in shapes:
        print(shape.describe())
