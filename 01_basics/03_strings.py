"""03_strings.py - Working with text: slicing, methods, and formatting."""

text = "  Python Is Fun  "

# Clean up the text
clean = text.strip()
print("Stripped:", clean)

# Change the case
print("Upper:", clean.upper())
print("Lower:", clean.lower())
print("Title:", clean.title())

# Indexing and slicing (counting starts at 0)
word = "Programming"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("First four:", word[:4])
print("Reversed:", word[::-1])

# Searching and replacing
sentence = "I like apples and apples like me"
print("Count of 'apples':", sentence.count("apples"))
print("Replaced:", sentence.replace("apples", "pears"))

# Splitting and joining
words = sentence.split()
print("Words:", words)
print("Joined with dashes:", "-".join(words))

# f-string formatting
name, price = "Notebook", 3.5
print(f"{name} costs ${price:.2f}")
