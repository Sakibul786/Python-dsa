# Problem 1:
# Given a list of numbers, count how many times
# each number appears.
#
# Example:
# numbers = [1, 2, 2, 3, 1, 4, 2]
#
# Expected Output:
# 1 → 2
# 2 → 3
# 3 → 1
# 4 → 1

numbers = [1, 2, 2, 3, 1, 4, 2]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Problem 1:", frequency)