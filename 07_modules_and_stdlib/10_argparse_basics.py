"""10_argparse_basics.py - Give your script command-line options.

Try it in a terminal:
    python 10_argparse_basics.py Ada --times 2 --shout
"""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--times", type=int, default=1, help="how many times")
    parser.add_argument("--shout", action="store_true", help="use capital letters")
    return parser


def main(arguments=None) -> None:
    args = build_parser().parse_args(arguments)
    message = f"Hello, {args.name}!"
    if args.shout:
        message = message.upper()
    for _ in range(args.times):
        print(message)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        main()
    else:
        # No options given, so run a built-in demo
        main(["Ada", "--times", "2", "--shout"])
