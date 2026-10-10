"""01_string_cleaning.py - Clean messy text."""

raw = "  Hello,   WORLD!  \n\t  "

clean = raw.strip().lower()
print("Cleaned:", repr(clean))

# Remove punctuation and extra spaces
import string

messy = "Hello, World!!! How's it going?"
no_punct = "".join(ch for ch in messy if ch not in string.punctuation)
normalised = " ".join(no_punct.split())
print("Normalised:", normalised)

# Replace multiple spaces
spaced = "too   many    spaces"
print("Fixed spaces:", " ".join(spaced.split()))
