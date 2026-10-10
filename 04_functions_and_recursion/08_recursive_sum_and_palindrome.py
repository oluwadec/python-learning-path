"""08_recursive_sum_and_palindrome.py - More recursive patterns."""


def recursive_sum(numbers: list) -> int:
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


print("Sum:", recursive_sum([1, 2, 3, 4, 5]))
print("'racecar' palindrome?", is_palindrome("racecar"))
print("'hello' palindrome?", is_palindrome("hello"))
print("Reverse 'python':", reverse_string("python"))
