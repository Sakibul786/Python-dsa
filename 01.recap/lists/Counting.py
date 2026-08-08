# Problem 3:
# Given a list of numbers, count how many even numbers
# are present in the list.
#
# Example:
# numbers = [10, 15, 22, 33, 40, 51, 60]
#
# Expected Output:
# 4


numbers = [10, 15, 22, 33, 40, 51, 60]

count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("Problem 3:", count)