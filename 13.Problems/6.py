"""
PROBLEM:

You are given an array of coin denominations and an integer amount.

Find the minimum number of coins needed to make the given amount.

You can use each coin denomination an unlimited number of times.

If the amount cannot be formed using the given coins,
return -1.

EXAMPLE:

coins = [1, 2, 5]
amount = 11

Expected Output:
3

Explanation:
11 = 5 + 5 + 1

APPROACH:

Use Dynamic Programming.

1. Create a DP array of size amount + 1.
2. Initialize every position with infinity.
3. Set dp[0] = 0 because zero coins are needed to make amount 0.
4. For each amount, try every available coin.
5. If a coin can be used, update the minimum number of coins.
6. Return the result for the target amount.

"""


def coin_change(coins, amount):
    if amount < 0:
        return -1

    if any(coin <= 0 for coin in coins):
        raise ValueError("Coin denominations must be positive.")

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


# Test Case 1
coins = [1, 2, 5]
amount = 11

print(coin_change(coins, amount))



# Test Case 2
coins = [2]
amount = 3

print(coin_change(coins, amount))



# Test Case 3
coins = [1]
amount = 0

print(coin_change(coins, amount))



# Test Case 4
coins = [1, 3, 4]
amount = 6

print(coin_change(coins, amount))





# Test Case 5
coins = [2, 5, 10]
amount = 18

print(coin_change(coins, amount))





"""
DRY RUN:

coins = [1, 2, 5]
amount = 6

Initial DP:
[0, inf, inf, inf, inf, inf, inf]

For amount 1:
1 = 1
dp[1] = 1

For amount 2:
2 = 1 + 1
2 = 2
dp[2] = 1

For amount 3:
3 = 2 + 1
dp[3] = 2

For amount 4:
4 = 2 + 2
dp[4] = 2

For amount 5:
5 = 5
dp[5] = 1

For amount 6:
6 = 5 + 1
dp[6] = 2

Final DP:
[0, 1, 1, 2, 2, 1, 2]

Answer:
2


WHY USE DYNAMIC PROGRAMMING?

The same smaller amounts are used repeatedly
while calculating larger amounts.

DP stores previously calculated answers
to avoid repeating the same work.

WHY INITIALIZE WITH INFINITY?

Initially, we assume that no amount can be formed.
Whenever a valid combination is found,
we update the minimum coin count.

COMPLEXITY:

N = Number of coin denominations
A = Target amount

Time Complexity:
O(N * A)

Space Complexity:
O(A)

IMPORTANT:

A greedy approach does not always give the optimal answer.

For example:
coins = [1, 3, 4]
amount = 6

Greedy chooses:
4 + 1 + 1 = 3 coins

Optimal answer:
3 + 3 = 2 coins

Dynamic Programming guarantees the optimal answer.
"""