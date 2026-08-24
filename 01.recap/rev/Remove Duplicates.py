# Problem 3:
# Create a function named remove_duplicates(numbers)
# that returns a new list without duplicates.
#
# Keep the original order.
#
# Do NOT use set().
#
# Example:
# numbers = [1, 2, 2, 3, 1, 4, 3]
#
# Expected Output:
# [1, 2, 3, 4]

def remove_duplicates(numbers):

    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


numbers = [1, 2, 2, 3, 1, 4, 3]

print("Problem 3:", remove_duplicates(numbers))