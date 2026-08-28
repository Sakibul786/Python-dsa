# Find the time and space complexity.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for first in numbers:
    for second in numbers:
        print(first, second)

# Answer:
# Time Complexity: O(n²)
# Space Complexity: O(1)

# Explanation:
# First loop: O(n)
# Nested loop: O(n²)
#
# Total:
# O(n) + O(n²)
#
# O(n²) is the dominant term.
# Therefore:
# O(n) + O(n²) = O(n²)