# Problem 2:
# Given a list of numbers, count how many odd numbers
# are present.
#
# Example:
# numbers = [10, 15, 22, 33, 40, 51, 67]
#
# Expected Output:
# 4

numbers = [10, 15, 22, 33, 40, 51, 67]

count = 0

for num in numbers:
    if num % 2 != 0:
        count += 1

print("Problem 2:", count)