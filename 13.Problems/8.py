
"""
Problem: Longest Common Subsequence (LCS)

Description:
Given two strings, find the length of their longest common subsequence.

A subsequence is a sequence that can be formed by deleting some characters
without changing the order of the remaining characters.

Example:
Input:
text1 = "abcde"
text2 = "ace"

Output:
3

Explanation:
The longest common subsequence is "ace".
Its length is 3.

Another Example:
Input:
text1 = "abc"
text2 = "def"

Output:
0

Approach: Dynamic Programming (2D DP)

1. Create a DP table with (m + 1) rows and (n + 1) columns.
2. dp[i][j] represents the LCS length of:
   - The first i characters of text1.
   - The first j characters of text2.
3. If the current characters match:
      dp[i][j] = 1 + dp[i-1][j-1]
4. Otherwise:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
5. The final answer is dp[m][n].

Solution:
"""

def longest_common_subsequence(text1, text2):
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



test_cases = [
    ("abcde", "ace", 3),
    ("abc", "def", 0),
    ("abc", "abc", 3),
    ("abc", "ac", 2),
    ("", "abc", 0),
    ("AGGTAB", "GXTXAYB", 4)
]

for text1, text2, expected in test_cases:
    result = longest_common_subsequence(text1, text2)

    print("Input:", text1, text2)
    print("Output:", result)
    print("Expected:", expected)
    print("Passed:", result == expected)
    print()


"""

Time Complexity: O(m * n)
Space Complexity: O(m * n)

Where:
m = Length of the first string
n = Length of the second string

Interview Follow-up:
Can you optimize the space complexity from O(m * n) to O(n)
using only two DP rows?
"""
