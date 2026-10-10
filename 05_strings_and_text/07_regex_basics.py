"""07_regex_basics.py - Find patterns in text with regular expressions."""

import re

text = "Contact ada@example.com or ben.o@school.edu. Call 0801-555-0199 on 2024-03-15."

# findall returns every match
emails = re.findall(r"[\w.]+@[\w.]+\.\w+", text)
print("Emails:", emails)

dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print("Dates:", dates)

# search finds the first match; groups pull out parts of it
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if match:
    year, month, day = match.groups()
    print(f"Year {year}, month {month}, day {day}")

# sub replaces matches
hidden = re.sub(r"\d", "#", "Card 1234 5678")
print("Hidden:", hidden)

# A simple check: does the whole string look like a username?
print("Valid username?", bool(re.fullmatch(r"[a-z][a-z0-9_]{2,11}", "ada_99")))
