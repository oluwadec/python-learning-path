"""08_prime_numbers.py - Find prime numbers."""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    # Only check divisors up to the square root
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def sieve(limit: int) -> list:
    """Sieve of Eratosthenes: a fast way to find all primes up to limit."""
    is_prime_flags = [True] * (limit + 1)
    is_prime_flags[0:2] = [False, False]

    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime_flags[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime_flags[multiple] = False

    return [n for n, flag in enumerate(is_prime_flags) if flag]


def prime_factors(n: int) -> list:
    factors, divisor = [], 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


if __name__ == "__main__":
    print("Is 29 prime?", is_prime(29))
    print("Is 30 prime?", is_prime(30))
    print("Primes up to 50:", sieve(50))
    print("Factors of 360:", prime_factors(360))
