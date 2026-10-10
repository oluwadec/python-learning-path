"""08_hangman_simulation.py - Mini project: hangman with a list of guesses."""


def show_progress(word: str, guessed: set) -> str:
    return " ".join(letter if letter in guessed else "_" for letter in word)


def play_hangman(word: str, guesses: list, max_wrong: int = 6) -> bool:
    guessed = set()
    wrong = 0

    for letter in guesses:
        guessed.add(letter)
        if letter not in word:
            wrong += 1
        print(f"Guess {letter!r}: {show_progress(word, guessed)}   (wrong: {wrong}/{max_wrong})")

        if all(ch in guessed for ch in word):
            print("You won!")
            return True
        if wrong >= max_wrong:
            print(f"You lost. The word was '{word}'.")
            return False

    print("Out of guesses.")
    return False


if __name__ == "__main__":
    play_hangman("python", list("etaonphy"))
