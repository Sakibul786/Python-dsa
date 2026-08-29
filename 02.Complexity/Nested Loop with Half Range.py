# Find the time and space complexity.

n = 100

for i in range(n):
    for j in range(n // 2):
        print(i, j)

# Answer:
# Time Complexity: O(n²)
# Space Complexity: O(1)
#
# Explanation:
# Outer loop runs n times.
# Inner loop runs approximately n / 2 times.
#
# Total:
# n × (n / 2)
# = n² / 2
#
# Constants are ignored in Big O notation.
# Therefore:
# O(n² / 2) = O(n²)