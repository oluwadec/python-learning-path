"""04_return_multiple_values.py - Return several results at once."""


def min_max_avg(numbers: list) -> tuple:
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


def split_name(full: str) -> tuple:
    parts = full.split()
    first = parts[0]
    last = parts[-1] if len(parts) > 1 else ""
    return first, last


low, high, avg = min_max_avg([10, 3, 7, 20, 5])
print(f"Min={low}, Max={high}, Avg={avg:.1f}")

first, last = split_name("Ada Lovelace")
print(f"First: {first}, Last: {last}")
