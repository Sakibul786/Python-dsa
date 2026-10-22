
# Question 1:
# Find the minimum multiplication cost for a matrix chain.

def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1

    if n <= 0:
        return 0

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


print(
    "Minimum multiplication cost:",
    matrix_chain_multiplication([10, 30, 5, 60])
)


# Question 2:
# Return the optimal parenthesization of a matrix chain.

def matrix_chain_order(dimensions):
    n = len(dimensions) - 1

    if n <= 0:
        return 0, ""

    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def build_order(i, j):
        if i == j:
            return f"A{i + 1}"

        k = split[i][j]

        left = build_order(i, k)
        right = build_order(k + 1, j)

        return f"({left} x {right})"

    return dp[0][n - 1], build_order(0, n - 1)


cost, order = matrix_chain_order([10, 30, 5, 60])

print("Optimal cost:", cost)
print("Optimal order:", order)


# Question 3:
# Find the minimum cost to cut a stick at given positions.

def min_cost_to_cut_stick(length, cuts):
    positions = [0] + sorted(cuts) + [length]
    n = len(positions)

    dp = [[0] * n for _ in range(n)]

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float("inf")

            for k in range(i + 1, j):
                cost = (
                    dp[i][k]
                    + dp[k][j]
                    + positions[j] - positions[i]
                )

                dp[i][j] = min(dp[i][j], cost)

            if dp[i][j] == float("inf"):
                dp[i][j] = 0

    return dp[0][n - 1]


print(
    "Minimum cutting cost:",
    min_cost_to_cut_stick(7, [1, 3, 4, 5])
)


# Question 4:
# Find the minimum cost to cut a stick using memoization.

from functools import lru_cache

def min_cost_to_cut_stick_memo(length, cuts):
    positions = [0] + sorted(cuts) + [length]

    @lru_cache(maxsize=None)
    def solve(left, right):
        if right - left <= 1:
            return 0

        best = float("inf")

        for k in range(left + 1, right):
            cost = (
                positions[right] - positions[left]
                + solve(left, k)
                + solve(k, right)
            )

            best = min(best, cost)

        return best

    return solve(0, len(positions) - 1)


print(
    "Minimum cutting cost with memoization:",
    min_cost_to_cut_stick_memo(7, [1, 3, 4, 5])
)


# Question 5:
# Explain the difference between MCM and Partition DP.
#
# Answer:
# MCM selects the best split to minimize matrix multiplication cost.
# Partition DP divides a problem into smaller intervals and combines
# their optimal results to find the minimum or maximum cost.


# Question 6:
# State the time and auxiliary space complexities.
#
# Answer:
# Matrix Chain Multiplication:
# Time: O(n^3)
# Auxiliary space: O(n^2)
#
# Matrix Chain Order Reconstruction:
# Time: O(n^3)
# Auxiliary space: O(n^2)
#
# Minimum Cost to Cut a Stick:
# Time: O(c^3)
# Auxiliary space: O(c^2)
#
# Memoized Stick Cutting:
# Time: O(c^3)
# Auxiliary space: O(c^2)
#
# Here, n is the number of matrices and c is the number of cuts.
