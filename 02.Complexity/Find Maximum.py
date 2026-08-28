# Find the time and space complexity.

numbers = [10, 25, 7, 40, 15]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)

# Answer:
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Explanation:
# The loop visits every element once.
# Therefore, the time complexity is O(n).
#
# Only a few variables are used regardless of input size.
# Therefore, the space complexity is O(1).