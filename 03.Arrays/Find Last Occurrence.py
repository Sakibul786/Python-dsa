# Create a function named last_occurrence(numbers, target)
# that returns the index of the last occurrence.
#
# Example:
# numbers = [1, 2, 2, 2, 4, 5]
# target = 2
#
# Expected Output:
# 3


def last_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            left = mid + 1

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result


numbers = [1, 2, 2, 2, 4, 5]

print(last_occurrence(numbers, 2))

# Time Complexity: O(log n)
# Space Complexity: O(1)