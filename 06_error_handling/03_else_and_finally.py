"""03_else_and_finally.py - Extra parts of a try block."""


def parse_number(text: str):
    try:
        value = int(text)
    except ValueError:
        print(f"  '{text}' is not an integer")
        return None
    else:
        # runs only when no exception happened
        print(f"  Parsed {value}")
        return value
    finally:
        # always runs, even if there was an error
        print("  (cleanup done)")


for item in ["42", "abc", "7"]:
    print(f"Trying {item!r}")
    parse_number(item)
