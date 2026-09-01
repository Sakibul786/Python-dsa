# Create a function named is_palindrome(numbers)
# that returns True if the list is a palindrome.
#
# Example:
# numbers = [1, 2, 3, 2, 1]
#
# Expected Output:
# True
#
# Example:
# numbers = [1, 2, 3, 4]
#
# Expected Output:
# False


def is_palindrome(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] != numbers[right]:
            return False

        left += 1
        right -= 1

    return True


print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome([1, 2, 3, 4]))

# Time Complexity: O(n)
# Space Complexity: O(1)