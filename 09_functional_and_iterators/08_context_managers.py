"""08_context_managers.py - Set up and clean up automatically with 'with'."""

from contextlib import contextmanager
import time


class Timer:
    """Measures how long the code inside the with-block takes."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"Block finished in {self.elapsed:.4f}s")
        return False                 # False = do not hide errors


@contextmanager
def announce(task: str):
    print(f"Starting {task}...")
    try:
        yield
    finally:
        print(f"Finished {task}.")


with Timer():
    total = sum(range(500_000))

with announce("cleanup"):
    print("  doing the work")

try:
    with announce("risky job"):
        raise RuntimeError("something broke")
except RuntimeError as error:
    print("Caught:", error)
