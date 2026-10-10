"""01_math_module.py - Useful mathematical functions."""

import math

print("pi:", math.pi)
print("sqrt(16):", math.sqrt(16))
print("ceil(3.2):", math.ceil(3.2))
print("floor(3.8):", math.floor(3.8))
print("factorial(5):", math.factorial(5))
print("gcd(48, 18):", math.gcd(48, 18))
print("log10(1000):", math.log10(1000))
print("radians(180):", math.radians(180))
print("sin(pi/2):", math.sin(math.pi / 2))

# Clamp a value between low and high
def clamp(value, low, high):
    return max(low, min(high, value))

print("clamp 15 to 0-10:", clamp(15, 0, 10))
