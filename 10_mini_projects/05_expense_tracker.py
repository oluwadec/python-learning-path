"""05_expense_tracker.py - Mini project: track spending by category."""

from collections import defaultdict

expenses = [
    {"item": "Bus pass", "category": "Transport", "amount": 45.00},
    {"item": "Lunch", "category": "Food", "amount": 12.50},
    {"item": "Notebook", "category": "School", "amount": 4.25},
    {"item": "Dinner", "category": "Food", "amount": 20.00},
    {"item": "Taxi", "category": "Transport", "amount": 15.75},
]


def total_by_category(items: list) -> dict:
    totals = defaultdict(float)
    for expense in items:
        totals[expense["category"]] += expense["amount"]
    return dict(totals)


def report(items: list, budget: float) -> None:
    totals = total_by_category(items)
    grand_total = sum(totals.values())

    print(f"{'Category':<12}{'Spent':>8}")
    for category, amount in sorted(totals.items(), key=lambda p: p[1], reverse=True):
        print(f"{category:<12}{amount:>8.2f}")

    print(f"{'TOTAL':<12}{grand_total:>8.2f}")
    left = budget - grand_total
    print(f"Budget left: {left:.2f}" if left >= 0 else f"Over budget by {-left:.2f}")


if __name__ == "__main__":
    report(expenses, budget=100)
