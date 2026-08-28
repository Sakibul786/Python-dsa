# Find the time and space complexity.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for number in numbers:
    print(number)

# Answer:
# Time Complexity: O(n)
# Space Complexity: O(1)

# Explanation:
# First loop: O(n)
# Second loop: O(n)
#
# Total:
# O(n) + O(n)
# = O(2n)
#
# Constants are ignored in Big O notation.
# Therefore:
# O(2n) = O(n)