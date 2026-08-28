# Find the time and space complexity.

numbers = [1, 2, 3, 4, 5]

for first in numbers:
    for second in numbers:
        print(first, second)

# Answer:
# Time Complexity: O(n²)
# Space Complexity: O(1)

# Explanation:
# The outer loop runs n times.
# For every iteration of the outer loop,
# the inner loop also runs n times.
#
# Total operations:
# n × n = n²