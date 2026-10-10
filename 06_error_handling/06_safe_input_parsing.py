"""06_safe_input_parsing.py - Turn messy text into clean values safely."""


def to_int(text: str, default: int = 0) -> int:
    try:
        return int(text.strip())
    except (ValueError, AttributeError):
        return default


def parse_yes_no(text: str):
    answer = text.strip().lower()
    if answer in ("y", "yes", "true", "1"):
        return True
    if answer in ("n", "no", "false", "0"):
        return False
    return None      # unknown answer


def parse_price(text: str) -> float:
    """Accept values like '$1,250.50'."""
    cleaned = text.replace("$", "").replace(",", "").strip()
    return float(cleaned)


if __name__ == "__main__":
    print([to_int(x) for x in ["42", " 7 ", "oops", ""]])
    print([parse_yes_no(x) for x in ["Yes", "n", "maybe"]])
    print(parse_price("$1,250.50"))
