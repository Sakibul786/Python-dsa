# Find the time and space complexity.

i = 1

while i < n:
    print(i)
    i = i * 2

# Answer:
# Time Complexity: O(log n)
# Space Complexity: O(1)

# Explanation:
# The value of i doubles after every iteration.
#
# Example:
# 1 → 2 → 4 → 8 → 16 → 32 → ...
#
# The number of iterations grows logarithmically.