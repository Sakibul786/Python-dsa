# Problem 1:
# Create a function named find_max(numbers)
# that returns the largest number from a list.
#
# Example:
# numbers = [10, 25, 7, 40, 15]
#
# Expected Output:
# 40

def find_max(numbers):

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


numbers = [10, 25, 7, 40, 15]

print("Problem 1:", find_max(numbers))