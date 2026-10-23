
# Question 1:
# Find the number of ways to climb n stairs.
# You can climb either one or two steps at a time.

def climb_stairs(n):
    if n < 0:
        return 0

    dp = [0] * (n + 2)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] += dp[i - 1]

        if i >= 2:
            dp[i] += dp[i - 2]

    return dp[n]


print("Climbing stairs:", climb_stairs(5))


# Question 2:
# Find the minimum number of coins required to make an amount.
# Return -1 if the amount cannot be formed.

def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]


print("Minimum coins:", coin_change([1, 2, 5], 11))


# Question 3:
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


# Question 4:
# Find the maximum sum of non-adjacent elements.
# The selected elements must not be adjacent.

def house_robber(numbers):
    previous_two = 0
    previous_one = 0

    for number in numbers:
        current = max(
            previous_one,
            previous_two + number
        )

        previous_two = previous_one
        previous_one = current

    return previous_one


print("Maximum non-adjacent sum:", house_robber([2, 7, 9, 3, 1]))


# Question 5:
# Find the length of the Longest Increasing Subsequence.
# Use an O(n log n) approach.

from bisect import bisect_left

def lis_length(numbers):
    tails = []

    for number in numbers:
        index = bisect_left(tails, number)

        if index == len(tails):
            tails.append(number)
        else:
            tails[index] = number

    return len(tails)


print(
    "LIS length:",
    lis_length([10, 9, 2, 5, 3, 7, 101, 18])
)


# Question 6:
# Solve the 0/1 Knapsack problem using one-dimensional DP.

def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                value + dp[current_capacity - weight]
            )

    return dp[capacity]


print(
    "Knapsack maximum value:",
    knapsack([1, 2, 3], [10, 15, 40], 5)
)




# Climbing Stairs:
# Time: O(n), Space: O(n)
#
# Coin Change:
# Time: O(amount * number_of_coins)
# Space: O(amount)
#
# LCS:
# Time: O(m * n), Space: O(m * n)
#
# House Robber:
# Time: O(n), Space: O(1)
#
# LIS:
# Time: O(n log n), Space: O(n)
#
# 0/1 Knapsack:
# Time: O(n * capacity), Space: O(capacity)
