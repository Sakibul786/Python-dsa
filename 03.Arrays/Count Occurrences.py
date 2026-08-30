# Create a function named count_occurrences(numbers, target)
# that returns the number of times the target appears.
#
# Example:
# numbers = [1, 2, 2, 3, 2, 4]
# target = 2
#
# Expected Output:
# 3


def count_occurrences(numbers, target):
    count = 0

    for number in numbers:
        if number == target:
            count += 1

    return count


numbers = [1, 2, 2, 3, 2, 4]

print(count_occurrences(numbers, 2))

# Time Complexity: O(n)
# Space Complexity: O(1)