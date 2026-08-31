# Create a function named first_occurrence(numbers, target)
# that returns the index of the first occurrence.
#
# The list is sorted in ascending order.
#
# Example:
# numbers = [1, 2, 2, 2, 4, 5]
# target = 2
#
# Expected Output:
# 1


def first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            right = mid - 1

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result


numbers = [1, 2, 2, 2, 4, 5]

print(first_occurrence(numbers, 2))

# Time Complexity: O(log n)
# Space Complexity: O(1)