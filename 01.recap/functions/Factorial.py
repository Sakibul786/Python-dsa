# Problem 2:
# Create a recursive function to calculate
# the factorial of a number.
#
# Example:
# n = 5
#
# Expected Output:
# 120
#
# Because:
# 5 × 4 × 3 × 2 × 1 = 120

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("Problem 2:", factorial(5))