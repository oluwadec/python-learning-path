"""09_gcd_and_lcm.py - Greatest common divisor and least common multiple."""


def gcd(a: int, b: int) -> int:
    """Euclid's algorithm: keep replacing (a, b) with (b, a % b)."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def simplify_fraction(top: int, bottom: int) -> tuple:
    divisor = gcd(top, bottom)
    return top // divisor, bottom // divisor


if __name__ == "__main__":
    print("GCD(48, 18):", gcd(48, 18))
    print("LCM(4, 6):", lcm(4, 6))
    print("48/18 simplified:", simplify_fraction(48, 18))
