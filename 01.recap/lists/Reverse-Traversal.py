# Problem 4:
# Given a list of numbers, create a new list containing
# the elements in reverse order.
#
# Do NOT use:
#   reverse()
#   [::-1]
#
# Example:
# numbers = [1, 2, 3, 4, 5]
#
# Expected Output:
# [5, 4, 3, 2, 1]


numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Problem 4:", reversed_list)
