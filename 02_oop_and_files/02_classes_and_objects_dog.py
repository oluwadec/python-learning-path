"""02_classes_and_objects_dog.py - Your first class and some objects."""


class Dog:
    """A blueprint for making dog objects."""

    species = "Canis familiaris"  # shared by every dog (class attribute)

    def __init__(self, name: str, age: int):
        # __init__ runs when a new Dog is created
        self.name = name
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says Woof!"

    def birthday(self) -> None:
        self.age += 1

    def __str__(self) -> str:
        return f"{self.name} ({self.age} years old)"


if __name__ == "__main__":
    # Each object has its own data
    rex = Dog("Rex", 3)
    bella = Dog("Bella", 5)

    print(rex)
    print(bella.bark())

    rex.birthday()
    print("After birthday:", rex)
    print("Species:", Dog.species)
