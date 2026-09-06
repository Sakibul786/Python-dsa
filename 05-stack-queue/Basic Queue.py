
# Implement a queue and perform enqueue and dequeue operations.

from collections import deque

queue = deque()

# Enqueue elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Peek at the front element
print("Front:", queue[0])

# Dequeue the front element
removed = queue.popleft()

print("Removed:", removed)
print("Queue:", queue)