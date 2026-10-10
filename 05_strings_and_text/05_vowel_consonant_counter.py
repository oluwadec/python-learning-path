"""05_vowel_consonant_counter.py - Count vowels and consonants."""

VOWELS = set("aeiou")


def count_letters(text: str) -> dict:
    vowels = consonants = 0
    for ch in text.lower():
        if ch.isalpha():
            if ch in VOWELS:
                vowels += 1
            else:
                consonants += 1
    return {"vowels": vowels, "consonants": consonants}


sample = "Programming is fun"
result = count_letters(sample)
print(f"Text: {sample!r}")
print(f"Vowels: {result['vowels']}, Consonants: {result['consonants']}")
