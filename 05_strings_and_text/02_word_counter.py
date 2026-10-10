"""02_word_counter.py - Count words in text."""

from collections import Counter

text = """
Python is a great language. Python is easy to learn.
Many people love Python because it is readable.
"""

words = text.lower().split()
# Remove trailing punctuation from words
clean_words = [w.strip(".,!?") for w in words]
counts = Counter(clean_words)

print("Total words:", len(clean_words))
print("Unique words:", len(counts))
print("Most common:")
for word, count in counts.most_common(5):
    print(f"  {word}: {count}")
