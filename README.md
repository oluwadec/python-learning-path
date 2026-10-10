# Python Learning Path

A beginner-friendly collection of **100 small Python programs**, organised into 10 modules. Each file is short, focused on one idea, and has a few clear comments. Every script runs on its own and needs **no input and no extra libraries**, so you can run any file and immediately see what it does.

## Getting Started

You need Python 3.9 or newer.

```bash
git clone https://github.com/oluwadec/python-learning-path.git
cd python-learning-path
python 01_basics/03_strings.py        # use python3 on macOS/Linux
```

Exception: `01_basics/02_grade_calculator.py` is interactive and asks you to type scores.

## How to Use This Repo

1. Work through the folders in order. Each module builds on the one before it.
2. Read the file, run it, then **change something** (a value, a condition, a loop) and run it again.
3. Try to write each program yourself from scratch before looking at the solution.

## Modules

| Folder | Topic | What you will practise |
|--------|-------|------------------------|
| `01_basics` | Python fundamentals | Variables, strings, lists, dictionaries, loops, small programs like a to-do list and calculator |
| `02_oop_and_files` | Classes and files | Classes, inheritance, encapsulation, polymorphism, dataclasses, text/CSV/JSON files, `pathlib` |
| `03_data_structures` | Storing data | Lists, tuples, sets, nested data, stacks, queues, sorting, `Counter` and `defaultdict` |
| `04_functions_and_recursion` | Functions | Default and keyword arguments, `*args`/`**kwargs`, scope, closures, recursion, memoization |
| `05_strings_and_text` | Working with text | Cleaning, counting, ciphers, password checks, regular expressions, formatting |
| `06_error_handling` | Handling problems | `try`/`except`, custom exceptions, retries, logging, assertions, data validation |
| `07_modules_and_stdlib` | Standard library | `math`, `random`, `datetime`, `itertools`, `statistics`, `argparse`, your own modules |
| `08_algorithms` | Algorithms | Linear and binary search, five sorting algorithms, primes, GCD, classic problems |
| `09_functional_and_iterators` | Pythonic tools | Comprehensions, generators, iterators, decorators, context managers, enums |
| `10_mini_projects` | Putting it together | Bank, library, contacts, tic-tac-toe, expenses, quiz, text adventure, ATM |

## Folder Layout

```
python-learning-path/
├── 01_basics/                    10 files
├── 02_oop_and_files/             10 files
├── 03_data_structures/           10 files
├── 04_functions_and_recursion/   10 files
├── 05_strings_and_text/          10 files
├── 06_error_handling/            10 files
├── 07_modules_and_stdlib/        10 files
├── 08_algorithms/                10 files
├── 09_functional_and_iterators/  10 files
├── 10_mini_projects/             10 files
└── README.md
```

## Conventions Used

- **Numbered file names** show the suggested reading order, and the rest of the name says what the file teaches.
- **`if __name__ == "__main__":`** appears in files that define reusable functions or classes, so the demo only runs when you execute the file directly.
- **File examples are safe.** Programs that write files use a temporary folder that is deleted afterwards, so they never leave stray files on your computer.
- **Random examples use a fixed seed**, so you get the same output each time and can compare with the comments.

## Where to Go Next

- Re-build a mini project with your own twist (save data to JSON, add new features).
- Add unit tests with `unittest` or `pytest`.
- Explore virtual environments and installing packages with `pip`.
- Try a small web, data, or automation project using what you have learned.

Happy coding!
