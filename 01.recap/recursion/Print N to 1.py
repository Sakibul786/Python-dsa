# Problem 2:
# Create a recursive function that prints
# numbers from n to 1.
#
# Example:
# n = 5
#
# Expected Output:
# 5
# 4
# 3
# 2
# 1

def print_reverse(n):

    if n == 0:
        return

    print(n)

    print_reverse(n - 1)


print_reverse(5)