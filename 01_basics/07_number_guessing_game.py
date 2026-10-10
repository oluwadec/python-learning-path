"""07_number_guessing_game.py - A guessing game where the computer plays itself."""

import random


def play_round(secret: int, low: int = 1, high: int = 100) -> int:
    """Guess by halving the range each time. Returns the number of tries."""
    tries = 0
    while True:
        guess = (low + high) // 2
        tries += 1
        if guess == secret:
            return tries
        elif guess < secret:
            print(f"  {guess} is too low")
            low = guess + 1
        else:
            print(f"  {guess} is too high")
            high = guess - 1


if __name__ == "__main__":
    random.seed(7)  # fixed seed so the output is the same every run
    secret_number = random.randint(1, 100)
    print(f"Secret number is {secret_number}. Let's guess it!")
    attempts = play_round(secret_number)
    print(f"Found it in {attempts} tries.")
