"""06_temperature_converter.py - Convert between Celsius and Fahrenheit."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def describe(celsius: float) -> str:
    """Give a simple description of the temperature."""
    if celsius < 10:
        return "cold"
    elif celsius < 25:
        return "mild"
    return "hot"


if __name__ == "__main__":
    for c in [-5, 0, 18, 30, 100]:
        f = celsius_to_fahrenheit(c)
        print(f"{c:>4}°C = {f:>6.1f}°F ({describe(c)})")

    print(f"98.6°F = {fahrenheit_to_celsius(98.6):.1f}°C")
