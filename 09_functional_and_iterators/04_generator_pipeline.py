"""04_generator_pipeline.py - Chain generators like an assembly line."""


def read_lines(text: str):
    for line in text.strip().splitlines():
        yield line


def parse_numbers(lines):
    for line in lines:
        name, value = line.split(",")
        yield name.strip(), int(value)


def only_big(records, minimum: int):
    for name, value in records:
        if value >= minimum:
            yield name, value


data = """
apples, 12
pears, 3
mangoes, 25
grapes, 8
"""

# Each stage handles one item at a time, so nothing big is stored
pipeline = only_big(parse_numbers(read_lines(data)), minimum=10)

for name, value in pipeline:
    print(f"{name}: {value}")
