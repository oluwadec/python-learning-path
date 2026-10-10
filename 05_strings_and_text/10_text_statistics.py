"""10_text_statistics.py - Measure a paragraph."""

paragraph = (
    "Learning Python is rewarding. It rewards practice. "
    "Short sentences help. Longer ones appear when ideas grow complex."
)

words = paragraph.split()
sentences = [s.strip() for s in paragraph.replace("!", ".").replace("?", ".").split(".") if s.strip()]

print("Characters:", len(paragraph))
print("Words:", len(words))
print("Sentences:", len(sentences))
print("Average word length:", round(sum(len(w) for w in words) / len(words), 1))
print("Average sentence length:", round(len(words) / len(sentences), 1))
print("Longest word:", max(words, key=len))
