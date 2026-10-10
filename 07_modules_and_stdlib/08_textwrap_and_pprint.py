"""08_textwrap_and_pprint.py - Make long text and data easy to read."""

import textwrap
from pprint import pprint

long_text = (
    "Python was created by Guido van Rossum and first released in 1991. "
    "It is known for its readable code and gentle learning curve."
)

print("--- Wrapped to 40 characters ---")
print(textwrap.fill(long_text, width=40))

print("\n--- Shortened ---")
print(textwrap.shorten(long_text, width=50, placeholder="..."))

print("\n--- Indented ---")
print(textwrap.indent("line one\nline two", "    "))

print("\n--- Pretty print ---")
data = {"name": "Ada", "skills": ["python", "maths", "logic"], "address": {"city": "Lagos", "zip": "100001"}}
pprint(data, width=40)
