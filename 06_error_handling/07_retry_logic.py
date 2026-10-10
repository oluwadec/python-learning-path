"""07_retry_logic.py - Try again when something fails."""

import time

attempt_log = {"count": 0}


def unreliable_task() -> str:
    """Pretend to be a flaky network call: fails twice, then works."""
    attempt_log["count"] += 1
    if attempt_log["count"] < 3:
        raise ConnectionError("network hiccup")
    return "data received"


def retry(task, attempts: int = 5, delay: float = 0.1):
    for number in range(1, attempts + 1):
        try:
            return task()
        except ConnectionError as error:
            print(f"Attempt {number} failed: {error}")
            if number == attempts:
                raise                   # give up after the last attempt
            time.sleep(delay)


if __name__ == "__main__":
    print("Result:", retry(unreliable_task))
