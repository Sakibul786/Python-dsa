
# Question 1:
# Find the length of the Longest Common Subsequence.

def lcs_length(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


print("LCS length:", lcs_length("abcde", "ace"))


# Question 2:
# Return one Longest Common Subsequence.

def lcs_sequence(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    result = []
    i = m
    j = n

    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            result.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return "".join(result)


print("LCS sequence:", lcs_sequence("abcde", "ace"))
print("LCS sequence:", lcs_sequence("abc", "bac"))


# Question 3:
# Find the length of the Longest Increasing Subsequence.
# Use the O(n^2) dynamic programming approach.

def lis_length(numbers):
    if not numbers:
        return 0

    n = len(numbers)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


numbers = [10, 9, 2, 5, 3, 7, 101, 18]

print("LIS length:", lis_length(numbers))


# Question 4:
# Return one Longest Increasing Subsequence.

def lis_sequence(numbers):
    n = len(numbers)

    if n == 0:
        return []

    dp = [1] * n
    previous = [-1] * n

    for i in range(n):
        for j in range(i):
            if numbers[j] < numbers[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    previous[i] = j

    end = dp.index(max(dp))
    result = []

    while end != -1:
        result.append(numbers[end])
        end = previous[end]

    result.reverse()
    return result


print("LIS sequence:", lis_sequence(numbers))


# Question 5:
# Solve LIS using binary search in O(n log n) time.

from bisect import bisect_left

def lis_length_optimized(numbers):
    tails = []

    for number in numbers:
        index = bisect_left(tails, number)

        if index == len(tails):
            tails.append(number)
        else:
            tails[index] = number

    return len(tails)


print("Optimized LIS length:", lis_length_optimized(numbers))


# Question 6:
# Explain the difference between subsequence and substring.
#
# Answer:
# A subsequence can skip elements while preserving their order.
# A substring must contain consecutive characters.
#
# Example:
# String: "abcde"
# Subsequence: "ace"
# Substring: "bcd"


# Question 7:
# Explain the difference between LCS and LIS.
#
# Answer:
# LCS finds a common subsequence between two sequences.
# LIS finds an increasing subsequence within one sequence.


# Question 8:
# State the time and auxiliary space complexities.
#
# Answer:
# LCS length:
# Time: O(m * n)
# Auxiliary space: O(m * n)
#
# LCS sequence reconstruction:
# Time: O(m * n)
# Auxiliary space: O(m * n)
#
# LIS using dynamic programming:
# Time: O(n^2)
# Auxiliary space: O(n)
#
# LIS using binary search:
# Time: O(n log n)
# Auxiliary space: O(n)