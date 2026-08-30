# Create a function named linear_search(numbers, target)
# that returns True if the target exists in the list.
# Otherwise, return False.
#
# Example:
# numbers = [10, 20, 30, 40, 50]
# target = 30
#
# Expected Output:
# True


def linear_search(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False


numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))

# Time Complexity: O(n)
# Space Complexity: O(1)