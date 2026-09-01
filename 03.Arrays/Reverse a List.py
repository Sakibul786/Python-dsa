# Create a function named reverse_list(numbers)
# that reverses the list in place.
#
# Do not use reverse() or slicing.
#
# Example:
# numbers = [1, 2, 3, 4, 5]
#
# Expected Output:
# [5, 4, 3, 2, 1]


def reverse_list(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


numbers = [1, 2, 3, 4, 5]

print(reverse_list(numbers))

# Time Complexity: O(n)
# Space Complexity: O(1)