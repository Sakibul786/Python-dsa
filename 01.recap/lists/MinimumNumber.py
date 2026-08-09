# Problem 1:
# Given a list of numbers, find the smallest number.
#
# Example:
# numbers = [45, 12, 78, 3, 56, 9]
#
# Expected Output:
# 3

numbers = [45, 12, 78, 3, 56, 9]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Problem 1:", minimum)