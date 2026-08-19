# Problem 3:
# Create a recursive function that returns
# the sum of numbers from 1 to n.
#
# Example:
# n = 5
#
# Expected Output:
# 15
#
# Because:
# 1 + 2 + 3 + 4 + 5 = 15

def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("Problem 3:", sum_numbers(5))