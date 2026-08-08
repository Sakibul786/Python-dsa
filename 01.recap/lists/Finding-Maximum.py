# Problem 2:
# Given a list of numbers, find the largest number.
#
# Example:
# numbers = [12, 45, 7, 89, 23, 56]
#
# Expected Output:
# 89


numbers = [12, 45, 7, 89, 23, 56]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Problem 2:", maximum)