# Problem 5:
# Given a list, move all zeroes to the end.
#
# The order of the non-zero elements must remain the same.
#
# Example:
# numbers = [0, 1, 0, 3, 12]
#
# Expected Output:
# [1, 3, 12, 0, 0]

numbers = [0, 1, 0, 3, 12]

result = []

zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

for i in range(zero_count):
    result.append(0)

print("Problem 5:", result)