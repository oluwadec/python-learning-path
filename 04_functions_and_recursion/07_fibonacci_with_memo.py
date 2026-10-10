"""07_fibonacci_with_memo.py - Speed up recursion with memory."""


def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n: int, cache: dict = None) -> int:
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


print("Naive fib(10):", fib_naive(10))
print("Memo  fib(30):", fib_memo(30))
print("Memo  fib(10):", fib_memo(10))
