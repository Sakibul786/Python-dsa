# Create a function named move_zeroes(numbers)
# that moves all zeroes to the end of the list.
#
# Maintain the relative order of non-zero elements.
#
# Modify the list in place.
#
# Example:
# numbers = [0, 1, 0, 3, 12]
#
# Expected Output:
# [1, 3, 12, 0, 0]


def move_zeroes(numbers):
    position = 0

    for current in range(len(numbers)):
        if numbers[current] != 0:
            numbers[position], numbers[current] = (
                numbers[current],
                numbers[position]
            )

            position += 1

    return numbers


numbers = [0, 1, 0, 3, 12]

print(move_zeroes(numbers))

# Time Complexity: O(n)
# Space Complexity: O(1)