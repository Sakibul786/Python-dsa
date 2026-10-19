# Question 1:
# Solve the 0/1 Knapsack problem using a two-dimensional DP table.

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]

            if weight <= current_capacity:
                take_value = (
                    value
                    + dp[i - 1][current_capacity - weight]
                )

                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    take_value
                )

    return dp[n][capacity]


weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 5

print("Maximum value:", knapsack(weights, values, capacity))


# Question 2:
# Solve the 0/1 Knapsack problem using O(capacity) extra space.

def knapsack_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            dp[current_capacity] = max(
                dp[current_capacity],
                value + dp[current_capacity - weight]
            )

    return dp[capacity]


print(
    "Optimized maximum value:",
    knapsack_optimized(weights, values, capacity)
)


# Question 3:
# Find the minimum number of coins required to make an amount.
# Return -1 if the amount cannot be formed.

def coin_change_min(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                previous = dp[current_amount - coin]

                if previous != float("inf"):
                    dp[current_amount] = min(
                        dp[current_amount],
                        previous + 1
                    )

    if dp[amount] == float("inf"):
        return -1

    return dp[amount]


print("Minimum coins:", coin_change_min([1, 2, 5], 11))
print("Impossible amount:", coin_change_min([2], 3))


# Question 4:
# Count the number of combinations that form an amount.
# Each coin denomination can be used unlimited times.
# Different orders of the same coins count as one combination.

def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] += dp[current_amount - coin]

    return dp[amount]


print("Number of combinations:", coin_change_ways([1, 2, 5], 5))


# Question 5:
# Return one optimal set of items for the 0/1 Knapsack problem.
# Return the selected item indices and their total value.

def knapsack_items(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]

            if weight <= current_capacity:
                take_value = (
                    value
                    + dp[i - 1][current_capacity - weight]
                )

                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    take_value
                )

    selected_indices = []
    current_capacity = capacity

    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            selected_indices.append(i - 1)
            current_capacity -= weights[i - 1]

    selected_indices.reverse()

    return selected_indices, dp[n][capacity]


indices, total_value = knapsack_items(
    [1, 2, 3],
    [10, 15, 40],
    5
)

print("Selected item indices:", indices)
print("Total value:", total_value)


# Question 6:
# Explain the difference between 0/1 Knapsack and Coin Change.
#
# Answer:
# In 0/1 Knapsack, each item can be selected at most once.
# In the standard Coin Change problems above, each denomination
# can be used unlimited times.


# Question 7:
# State the time and auxiliary space complexities.
#
# Answer:
# Two-dimensional Knapsack:
# Time: O(n * capacity)
# Auxiliary space: O(n * capacity)
#
# Optimized Knapsack:
# Time: O(n * capacity)
# Auxiliary space: O(capacity)
#
# Minimum Coin Change:
# Time: O(amount * number_of_coins)
# Auxiliary space: O(amount)
#
# Coin Change Combinations:
# Time: O(amount * number_of_coins)
# Auxiliary space: O(amount)