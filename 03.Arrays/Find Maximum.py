# Create a function named find_max(numbers)
# that returns the largest number in the list.
#
# Do NOT use max().
#
# Example:
# numbers = [10, 25, 7, 40, 15]
#
# Expected Output:
# 40


def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


numbers = [10, 25, 7, 40, 15]

print(find_max(numbers))

# Time Complexity: O(n)
# Space Complexity: O(1)