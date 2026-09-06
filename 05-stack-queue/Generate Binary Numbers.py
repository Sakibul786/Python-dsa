
# Generate the first n binary numbers using a queue.

from collections import deque

n = 5

queue = deque(["1"])
result = []

for _ in range(n):
    current = queue.popleft()

    result.append(current)

    queue.append(current + "0")
    queue.append(current + "1")

print(result)