"""06_stack_with_list.py - A stack: last in, first out."""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self) -> bool:
        return len(self.items) == 0


def is_balanced(text: str) -> bool:
    """Check that every bracket is closed in the right order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = Stack()
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in pairs:
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    for test in ["(a + b) * [c]", "((1 + 2)", "{[()]}", "(]"]:
        print(f"{test!r:18} balanced? {is_balanced(test)}")
