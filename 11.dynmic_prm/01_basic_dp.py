from functools import lru_cache


# Question 1:
# Calculate the nth Fibonacci number using normal recursion.

def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(6))


# Question 2:
# Calculate the nth Fibonacci number using memoization.

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n

    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


print(fibonacci_memo(10))


# Question 3:
# Calculate the nth Fibonacci number using tabulation.

def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]

    return dp[n]


print(fibonacci_tabulation(10))


# Question 4:
# Calculate the nth Fibonacci number using O(1) extra space.

def fibonacci_optimized(n):
    if n <= 1:
        return n

    previous_two = 0
    previous_one = 1

    for _ in range(2, n + 1):
        current = previous_two + previous_one
        previous_two = previous_one
        previous_one = current

    return previous_one


print(fibonacci_optimized(10))


# Question 5:
# Count the number of distinct ways to climb n stairs.
# You can climb either one stair or two stairs at a time.

def climbing_stairs(n):
    if n <= 2:
        return n

    previous_two = 1
    previous_one = 2

    for _ in range(3, n + 1):
        current = previous_two + previous_one
        previous_two = previous_one
        previous_one = current

    return previous_one


print(climbing_stairs(5))


# Question 6:
# Count climbing-stairs ways using memoization.

@lru_cache(maxsize=None)
def climbing_stairs_memo(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    return (
        climbing_stairs_memo(n - 1)
        + climbing_stairs_memo(n - 2)
    )


print(climbing_stairs_memo(5))


# Question 7:
# Calculate the minimum number of steps to reach n.
# From position 0, you can move forward one or two steps.
# Count the number of moves, not the number of possible paths.

def minimum_steps(n):
    if n < 0:
        return -1

    if n == 0:
        return 0

    if n <= 2:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for index in range(3, n + 1):
        dp[index] = 1 + min(dp[index - 1], dp[index - 2])

    return dp[n]


print(minimum_steps(5))


# Question 8:
# Explain the difference between memoization and tabulation.
#
# Answer:
# Memoization uses recursion and caches computed results.
# Tabulation fills a table iteratively, starting with smaller subproblems.


# Question 9:
# State the time and space complexity of Fibonacci tabulation.
#
# Answer:
# Time complexity: O(n).
# Auxiliary space: O(n) for the DP array.
# The optimized iterative version uses O(1) extra space.