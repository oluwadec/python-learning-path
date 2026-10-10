"""02_lambda_map_filter_reduce.py - Small functions for data pipelines."""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# lambda = a tiny function without a name
add_ten = lambda x: x + 10
print("add_ten(5):", add_ten(5))

print("map    :", list(map(lambda n: n * 2, numbers)))
print("filter :", list(filter(lambda n: n > 3, numbers)))

# reduce combines all items into one value
total = reduce(lambda a, b: a + b, numbers)
product = reduce(lambda a, b: a * b, numbers)
print("reduce sum:", total, "| product:", product)

# Combine them: sum of squares of the even numbers
result = sum(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print("Sum of even squares:", result)
