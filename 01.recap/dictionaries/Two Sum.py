# Problem 5:
# Given a list of numbers and a target,
# find two numbers whose sum equals the target.
#
# Example:
# numbers = [2, 7, 11, 15]
# target = 9
#
# Expected Output:
# [0, 1]
#
# Because:
# numbers[0] + numbers[1]
# = 2 + 7
# = 9

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(numbers):

    needed = target - num

    if needed in seen:
        print("Problem 5:", [seen[needed], i])
        break

    seen[num] = i