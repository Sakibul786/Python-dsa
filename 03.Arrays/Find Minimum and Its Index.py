# Create a function named find_min_with_index(numbers)
# that returns both the minimum value and its index.
#
# Do NOT use min().
#
# Example:
# numbers = [8, 3, 10, 2, 7]
#
# Expected Output:
# [2, 3]


def find_min_with_index(numbers):
    minimum = numbers[0]
    minimum_index = 0

    for index in range(len(numbers)):
        if numbers[index] < minimum:
            minimum = numbers[index]
            minimum_index = index

    return [minimum, minimum_index]


numbers = [8, 3, 10, 2, 7]

print(find_min_with_index(numbers))

# Time Complexity: O(n)
# Space Complexity: O(1)