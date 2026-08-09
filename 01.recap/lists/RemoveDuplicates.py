# Problem 4:
# Given a list containing duplicate numbers,
# create a new list without duplicates.
#
# Do NOT use set().
#
# Example:
# numbers = [1, 2, 2, 3, 4, 4, 5, 3]
#
# Expected Output:
# [1, 2, 3, 4, 5]

numbers = [1, 2, 2, 3, 4, 4, 5, 3]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Problem 4:", unique)