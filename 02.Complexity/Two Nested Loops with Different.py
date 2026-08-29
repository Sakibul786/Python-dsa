# Find the time and space complexity.

n = 5
m = 10

for i in range(n):
    for j in range(m):
        print(i, j)

# Answer:
# Time Complexity: O(n × m)
# Space Complexity: O(1)
#
# Explanation:
# The outer loop runs n times.
# The inner loop runs m times.
#
# Total operations:
# n × m
#
# Therefore:
# Time Complexity: O(nm)