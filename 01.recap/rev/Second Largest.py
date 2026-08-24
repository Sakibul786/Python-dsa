# Problem 1:
# Create a function named second_largest(numbers)
# that returns the second largest number.
#
# Do NOT use sort() or sorted().
#
# Example:
# numbers = [10, 5, 20, 8, 15]
#
# Expected Output:
# 15

def second_largest(numbers):

    largest = float("-inf")
    second = float("-inf")

    for num in numbers:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    return second


numbers = [10, 5, 20, 8, 15]

print("Problem 1:", second_largest(numbers))