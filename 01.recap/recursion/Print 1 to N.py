# Problem 1:
# Create a recursive function that prints
# numbers from 1 to n.
#
# Example:
# n = 5
#
# Expected Output:
# 1
# 2
# 3
# 4
# 5

def print_numbers(n):

    if n == 0:
        return

    print_numbers(n - 1)

    print(n)


print_numbers(5)