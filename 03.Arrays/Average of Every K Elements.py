# Create a function named window_averages(numbers, k)
# that returns the average of every k consecutive elements.
#
# Example:
# numbers = [1, 2, 3, 4, 5]
# k = 3
#
# Expected Output:
# [2.0, 3.0, 4.0]


def window_averages(numbers, k):
    result = []

    window_sum = sum(numbers[:k])
    result.append(window_sum / k)

    for right in range(k, len(numbers)):
        window_sum += numbers[right]
        window_sum -= numbers[right - k]

        result.append(window_sum / k)

    return result


numbers = [1, 2, 3, 4, 5]

print(window_averages(numbers, 3))

# Time Complexity: O(n)
# Space Complexity: O(n)