"""04_caesar_cipher.py - Shift letters by a fixed amount."""


def caesar(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


message = "Hello, Python!"
encoded = caesar(message, 3)
decoded = caesar(encoded, -3)
print("Original:", message)
print("Encoded :", encoded)
print("Decoded :", decoded)

# Brute-force a short cipher
cipher = "Khoor"
for s in range(26):
    print(f"shift {s:2}: {caesar(cipher, -s)}")
