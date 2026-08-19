# Problem 5:
# Create a recursive function to find
# the nth Fibonacci number.
#
# Fibonacci sequence:
#
# 0, 1, 1, 2, 3, 5, 8, 13...
#
# Example:
# n = 6
#
# Expected Output:
# 8

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print("Problem 5:", fibonacci(6))