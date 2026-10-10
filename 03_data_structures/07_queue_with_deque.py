"""07_queue_with_deque.py - A queue: first in, first out."""

from collections import deque

# deque is fast at adding/removing from both ends
line = deque()

line.append("Ada")
line.append("Ben")
line.append("Chi")
print("Waiting:", list(line))

served = line.popleft()        # the first person leaves
print("Served:", served)
print("Still waiting:", list(line))

# A deque with maxlen keeps only the newest items
recent = deque(maxlen=3)
for page in ["home", "about", "shop", "cart", "pay"]:
    recent.append(page)
print("Last 3 pages visited:", list(recent))
