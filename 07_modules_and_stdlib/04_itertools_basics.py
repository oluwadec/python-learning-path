"""04_itertools_basics.py - Tools for working with iterators."""

from itertools import count, cycle, islice, chain, combinations

# Infinite counter (take only a few)
print("Count from 5:", list(islice(count(5), 4)))

# Cycle through a list
colours = cycle(["red", "green", "blue"])
print("Cycle:", [next(colours) for _ in range(5)])

# Chain several sequences
print("Chain:", list(chain([1, 2], [3, 4], [5])))

# All pairs from a short list
print("Combinations:", list(combinations("ABCD", 2)))
