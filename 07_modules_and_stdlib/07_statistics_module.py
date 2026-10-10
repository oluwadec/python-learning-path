"""07_statistics_module.py - Mean, median, mode and more."""

import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Stdev:", round(statistics.stdev(data), 2))
print("Variance:", round(statistics.variance(data), 2))
