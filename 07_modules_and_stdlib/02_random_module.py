"""02_random_module.py - Generate random numbers and choices."""

import random

random.seed(42)  # fixed seed so output is repeatable

print("Random float 0-1:", random.random())
print("Random int 1-6:", random.randint(1, 6))
print("Random choice:", random.choice(["red", "green", "blue"]))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled:", numbers)

print("Sample of 3:", random.sample(range(1, 20), 3))
print("Gaussian around 10:", round(random.gauss(10, 2), 2))
