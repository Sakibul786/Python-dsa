# Create a function named two_sum_sorted(numbers, target)
# that returns the indexes of two numbers whose sum
# equals the target.
#
# The list is sorted in ascending order.
#
# Example:
# numbers = [1, 2, 4, 6, 8, 9]
# target = 10
#
# Expected Output:
# [0, 5]


def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return [-1, -1]


numbers = [1, 2, 4, 6, 8, 9]

print(two_sum_sorted(numbers, 10))

# Time Complexity: O(n)
# Space Complexity: O(1)