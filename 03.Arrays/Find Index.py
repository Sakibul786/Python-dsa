# Create a function named find_index(numbers, target)
# that returns the index of the target.
#
# If the target does not exist, return -1.
#
# Example:
# numbers = [10, 20, 30, 40, 50]
# target = 40
#
# Expected Output:
# 3


def find_index(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


numbers = [10, 20, 30, 40, 50]

print(find_index(numbers, 40))

# Time Complexity: O(n)
# Space Complexity: O(1)