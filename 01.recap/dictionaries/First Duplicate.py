# Problem 4:
# Given a list, find the first number that appears twice.
#
# Example:
# numbers = [5, 3, 1, 4, 3, 5]
#
# Expected Output:
# 3

numbers = [5, 3, 1, 4, 3, 5]

seen = set()

for num in numbers:
    if num in seen:
        print("Problem 4:", num)
        break

    seen.add(num)