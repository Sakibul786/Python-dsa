# Implement a stack and perform push, pop, and peek operations.

stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek at the top element
print("Top:", stack[-1])

# Pop the top element
removed = stack.pop()

print("Removed:", removed)
print("Stack:", stack)