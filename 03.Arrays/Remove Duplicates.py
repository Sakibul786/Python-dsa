# Create a function named remove_duplicates(numbers)
# that removes duplicates from a sorted list in place.
#
# Return the number of unique elements.
#
# Example:
# numbers = [1, 1, 2, 2, 3]
#
# Expected Output:
# 3
#
# The first three positions should contain:
# [1, 2, 3]


def remove_duplicates(numbers):
    if not numbers:
        return 0

    slow = 0

    for fast in range(1, len(numbers)):
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]

    return slow + 1


numbers = [1, 1, 2, 2, 3]

count = remove_duplicates(numbers)

print(count)
print(numbers[:count])

# Time Complexity: O(n)
# Space Complexity: O(1)