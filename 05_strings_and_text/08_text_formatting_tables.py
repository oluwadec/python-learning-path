"""08_text_formatting_tables.py - Print neat, aligned text."""

items = [("Notebook", 3, 2.5), ("Pen", 10, 0.75), ("Backpack", 1, 24.99)]

# < left align, > right align, ^ centre
print(f"{'Item':<12}{'Qty':>5}{'Price':>10}{'Total':>10}")
print("-" * 37)

grand_total = 0
for name, quantity, price in items:
    total = quantity * price
    grand_total += total
    print(f"{name:<12}{quantity:>5}{price:>10.2f}{total:>10.2f}")

print("-" * 37)
print(f"{'TOTAL':<12}{'':>5}{'':>10}{grand_total:>10.2f}")
