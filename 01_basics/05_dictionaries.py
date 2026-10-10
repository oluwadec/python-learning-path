"""05_dictionaries.py - Store data as key/value pairs."""

student = {"name": "Ada", "age": 20, "course": "Math"}

# Read values
print("Name:", student["name"])
print("Grade:", student.get("grade", "not set"))  # safe lookup with a default

# Add and update values
student["grade"] = "A"
student["age"] = 21

# Loop through keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# Check if a key exists
if "course" in student:
    print("Course found!")

# Count how often each word appears
words = ["red", "blue", "red", "green", "blue", "red"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Word counts:", counts)
