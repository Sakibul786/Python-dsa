# Create a function named integer_sqrt(n)
# that returns the integer square root of n.
#
# The result should be the largest integer x
# such that x * x <= n.
#
# Example:
# n = 16
# Expected Output:
# 4
#
# Example:
# n = 20
# Expected Output:
# 4
#
# Because:
# 4 * 4 = 16 <= 20
# 5 * 5 = 25 > 20


def integer_sqrt(n):
    if n < 2:
        return n

    left = 1
    right = n
    result = 1

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid

        if mid * mid < n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


print(integer_sqrt(16))
print(integer_sqrt(20))

# Time Complexity: O(log n)
# Space Complexity: O(1)