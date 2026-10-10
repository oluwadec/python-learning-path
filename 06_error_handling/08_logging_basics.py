"""08_logging_basics.py - Record what your program is doing."""

import logging
import sys

# Send log messages to the screen with a simple format
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)
logger = logging.getLogger("demo")


def divide(a: float, b: float):
    logger.info("Dividing %s by %s", a, b)
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        return None


print("Result:", divide(10, 2))
print("Result:", divide(10, 0))
logger.warning("This is a warning")
logger.debug("This debug message is hidden because level is INFO")
