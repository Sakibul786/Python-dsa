# Create a function named max_window_sum(numbers, k)
# that returns the maximum sum of any k consecutive elements.
#
# Example:
# numbers = [2, 1, 5, 1, 3, 2]
# k = 3
#
# Expected Output:
# 9


def max_window_sum(numbers, k):
    window_sum = sum(numbers[:k])
    maximum = window_sum

    for right in range(k, len(numbers)):
        window_sum += numbers[right]
        window_sum -= numbers[right - k]

        maximum = max(maximum, window_sum)

    return maximum


numbers = [2, 1, 5, 1, 3, 2]

print(max_window_sum(numbers, 3))

# Time Complexity: O(n)
# Space Complexity: O(1)