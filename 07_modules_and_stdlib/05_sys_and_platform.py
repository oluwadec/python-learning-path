"""05_sys_and_platform.py - Information about the running program."""

import sys
import platform

print("Python version:", sys.version.split()[0])
print("Platform:", platform.system(), platform.release())
print("Machine:", platform.machine())
print("Arguments:", sys.argv)
print("Max int size bits:", sys.maxsize.bit_length())

# Exit early (commented so the rest of the file can run)
# sys.exit(0)
