# Problem 4:
# Create a recursive function to calculate
# the factorial of n.
#
# Example:
# n = 5
#
# Expected Output:
# 120

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))