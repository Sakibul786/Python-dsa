# Create a function named binary_search(numbers, target)
# that returns the index of the target.
#
# Return -1 if the target does not exist.
#
# The list is sorted in ascending order.
#
# Example:
# numbers = [2, 5, 8, 12, 16, 20, 25]
# target = 16
#
# Expected Output:
# 4


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [2, 5, 8, 12, 16, 20, 25]

print(binary_search(numbers, 16))

# Time Complexity: O(log n)
# Space Complexity: O(1)