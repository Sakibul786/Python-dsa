# Given a sorted list and a target value,
# return the index where the target should be inserted
# to maintain sorted order.
#
# Example:
# numbers = [1, 3, 5, 6]
# target = 5
#
# Expected Output:
# 2
#
# Example:
# numbers = [1, 3, 5, 6]
# target = 2
#
# Expected Output:
# 1


def search_insert_position(numbers, target):
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

    return left


numbers = [1, 3, 5, 6]

print(search_insert_position(numbers, 5))
print(search_insert_position(numbers, 2))

# Time Complexity: O(log n)
# Space Complexity: O(1)