# Find the time and space complexity.

n = 5

for i in range(n):
    for j in range(n):
        print(i, j)

# Answer:
# Time Complexity: O(n²)
# Space Complexity: O(1)
#
# Explanation:
# The outer loop runs n times.
# The inner loop also runs n times for each outer iteration.
#
# Total operations:
# n × n = n²