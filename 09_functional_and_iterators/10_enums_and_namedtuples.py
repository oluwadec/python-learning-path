"""10_enums_and_namedtuples.py - Named choices and lightweight records."""

from collections import namedtuple
from enum import Enum


class Status(Enum):
    TODO = 1
    DOING = 2
    DONE = 3


Point = namedtuple("Point", ["x", "y"])

p = Point(3, 4)
print("Point:", p)
print("x =", p.x, "| y =", p.y)      # access by name, not just position

task_status = Status.DOING
print("Status:", task_status.name, "| value:", task_status.value)
print("Is it done?", task_status == Status.DONE)

# Loop through every choice
for status in Status:
    print(f"  {status.value}: {status.name}")

# Look up by value
print("Status 3 is", Status(3).name)
