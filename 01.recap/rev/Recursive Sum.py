# Problem 5:
# Create a recursive function named recursive_sum(n)
# that returns the sum from 1 to n.
#
# Example:
# n = 5
#
# Expected Output:
# 15
#
# Because:
# 1 + 2 + 3 + 4 + 5 = 15

def recursive_sum(n):

    if n == 0:
        return 0

    return n + recursive_sum(n - 1)


print("Problem 5:", recursive_sum(5))