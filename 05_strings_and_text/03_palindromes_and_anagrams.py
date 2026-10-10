"""03_palindromes_and_anagrams.py - Detect special word patterns."""


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def are_anagrams(a: str, b: str) -> bool:
    def sorted_letters(s: str) -> str:
        return "".join(sorted(ch.lower() for ch in s if ch.isalnum()))
    return sorted_letters(a) == sorted_letters(b)


for phrase in ["racecar", "A man a plan a canal Panama", "hello"]:
    print(f"{phrase!r:40} palindrome? {is_palindrome(phrase)}")

print("listen / silent:", are_anagrams("listen", "silent"))
print("hello / world:", are_anagrams("hello", "world"))
