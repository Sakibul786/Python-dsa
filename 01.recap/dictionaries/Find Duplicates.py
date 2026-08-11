# Problem 2:
# Given a list of numbers, find all numbers
# that appear more than once.
#
# Example:
# numbers = [1, 2, 3, 2, 4, 5, 1, 3]
#
# Expected Output:
# [1, 2, 3]

numbers = [1, 2, 3, 2, 4, 5, 1, 3]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

duplicates = []

for num, count in frequency.items():
    if count > 1:
        duplicates.append(num)

print("Problem 2:", duplicates)