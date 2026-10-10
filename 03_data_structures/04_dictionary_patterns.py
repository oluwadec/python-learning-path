"""04_dictionary_patterns.py - Common ways to use dictionaries."""

prices = {"apple": 0.5, "bread": 2.0, "milk": 1.2}

# Dictionary comprehension: build a new dictionary
discounted = {item: round(price * 0.9, 2) for item, price in prices.items()}
print("Discounted:", discounted)

# Keep only items that cost more than 1
expensive = {item: price for item, price in prices.items() if price > 1}
print("Expensive:", expensive)

# Merge two dictionaries (right side wins on conflicts)
extra = {"milk": 1.5, "eggs": 3.0}
merged = {**prices, **extra}
print("Merged:", merged)

# Swap keys and values
swapped = {price: item for item, price in prices.items()}
print("Swapped:", swapped)

# Find the cheapest item
cheapest = min(prices, key=prices.get)
print("Cheapest:", cheapest)
