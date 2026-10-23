
# Question 1:
# Implement basic bit manipulation operations.

def bit_operations(mask, index):
    is_set = (mask & (1 << index)) != 0
    set_result = mask | (1 << index)
    clear_result = mask & ~(1 << index)
    toggle_result = mask ^ (1 << index)

    return is_set, set_result, clear_result, toggle_result


print("Bit operations:", bit_operations(5, 1))


# Question 2:
# Solve the Traveling Salesperson Problem using Bitmask DP.
# Start at city 0, visit every city once, and return to city 0.

def tsp_min_cost(cost):
    n = len(cost)

    if n == 0 or any(len(row) != n for row in cost):
        raise ValueError("The cost matrix must be non-empty and square.")

    if n == 1:
        return 0

    total_masks = 1 << n
    infinity = float("inf")

    dp = [[infinity] * n for _ in range(total_masks)]
    dp[1][0] = 0

    for mask in range(total_masks):
        if (mask & 1) == 0:
            continue

        for current in range(n):
            if dp[mask][current] == infinity:
                continue

            if (mask & (1 << current)) == 0:
                continue

            for next_city in range(n):
                if mask & (1 << next_city):
                    continue

                next_mask = mask | (1 << next_city)
                new_cost = (
                    dp[mask][current]
                    + cost[current][next_city]
                )

                dp[next_mask][next_city] = min(
                    dp[next_mask][next_city],
                    new_cost
                )

    full_mask = total_masks - 1

    return min(
        dp[full_mask][city] + cost[city][0]
        for city in range(1, n)
    )


cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum TSP cost:", tsp_min_cost(cost))


# Question 3:
# Find the minimum cost to visit all cities from city 0.
# Return to city 0 is not required.

def minimum_cost_visit_all(cost):
    n = len(cost)

    if n == 0 or any(len(row) != n for row in cost):
        raise ValueError("The cost matrix must be non-empty and square.")

    if n == 1:
        return 0

    total_masks = 1 << n
    infinity = float("inf")

    dp = [[infinity] * n for _ in range(total_masks)]
    dp[1][0] = 0

    for mask in range(total_masks):
        for current in range(n):
            if dp[mask][current] == infinity:
                continue

            for next_city in range(n):
                if mask & (1 << next_city):
                    continue

                next_mask = mask | (1 << next_city)

                dp[next_mask][next_city] = min(
                    dp[next_mask][next_city],
                    dp[mask][current] + cost[current][next_city]
                )

    return min(dp[total_masks - 1])


print("Visit-all cost:", minimum_cost_visit_all(cost))


# Question 4:
# Count the number of set bits in an integer.

def count_set_bits(number):
    return number.bit_count()


print("Set bits:", count_set_bits(13))


# Question 5:
# Generate all subsets of a list using bitmasks.

def generate_subsets(numbers):
    n = len(numbers)
    subsets = []

    for mask in range(1 << n):
        subset = []

        for i in range(n):
            if mask & (1 << i):
                subset.append(numbers[i])

        subsets.append(subset)

    return subsets


print("Subsets:", generate_subsets([1, 2, 3]))


# Question 6:
# Explain the difference between Bitmask DP and ordinary DP.
#
# Answer:
# Ordinary DP uses states such as indices, capacities, or amounts.
# Bitmask DP uses a bitmask to represent a subset of selected items
# or visited nodes.


# Question 7:
# State the time and auxiliary space complexities.
#
# Answer:
# TSP using Bitmask DP:
# Time: O(n^2 * 2^n)
# Auxiliary space: O(n * 2^n)
#
# Minimum cost to visit all cities:
# Time: O(n^2 * 2^n)
# Auxiliary space: O(n * 2^n)
#
# Generate all subsets:
# Time: O(n * 2^n)
# Auxiliary space: O(n * 2^n), including the returned subsets.
#
# Count set bits:
# O(1) at the Python API level for a single integer operation.
