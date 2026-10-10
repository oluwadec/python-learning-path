"""05_polymorphism_animals.py - Different classes, same method name."""


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError("Child classes must define speak()")


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow"


class Cow(Animal):
    def speak(self) -> str:
        return f"{self.name} says Moo"


class Duck(Animal):
    def speak(self) -> str:
        return f"{self.name} says Quack"


if __name__ == "__main__":
    farm = [Cat("Tom"), Cow("Daisy"), Duck("Donald")]

    # The same call works for every animal, but each one answers differently
    for animal in farm:
        print(animal.speak())
