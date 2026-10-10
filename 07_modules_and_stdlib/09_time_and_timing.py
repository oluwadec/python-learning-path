"""09_time_and_timing.py - Measure how long code takes."""

import time


def slow_sum(n: int) -> int:
    total = 0
    for i in range(n):
        total += i
    return total


def timed(func, *args):
    """Run a function and return its result and how long it took."""
    start = time.perf_counter()
    result = func(*args)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    result, seconds = timed(slow_sum, 1_000_000)
    print("Loop result:", result)
    print("Took less than 5 seconds?", seconds < 5)

    result, seconds = timed(sum, range(1_000_000))
    print("Built-in sum result:", result)

    print("Pausing for a moment...")
    time.sleep(0.2)
    print("Done.")
