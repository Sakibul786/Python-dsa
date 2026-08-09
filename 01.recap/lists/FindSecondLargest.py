# Problem 3:
# Given a list of numbers, find the second largest number.
#
# Do NOT use:
#   sort()
#
# Example:
# numbers = [10, 5, 20, 8, 15]
#
# Expected Output:
# 15

numbers = [10, 5, 20, 8, 15]

largest = float("-inf")
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Problem 3:", second_largest)