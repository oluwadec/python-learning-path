"""03_datetime_basics.py - Work with dates and times."""

from datetime import datetime, date, timedelta

now = datetime.now()
print("Now:", now)
print("Formatted:", now.strftime("%Y-%m-%d %H:%M"))

birthday = date(2000, 5, 15)
today = date.today()
age_days = (today - birthday).days
print("Days since birthday:", age_days)

# Add or subtract time
in_a_week = today + timedelta(days=7)
print("One week from today:", in_a_week)

# Parse a string into a date
parsed = datetime.strptime("2024-12-25 18:30", "%Y-%m-%d %H:%M")
print("Parsed:", parsed)
