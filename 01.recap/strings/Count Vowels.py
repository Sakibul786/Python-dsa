# Problem 1:
# Given a string, count the number of vowels.
#
# Vowels are: a, e, i, o, u
#
# Example:
# text = "programming"
#
# Expected Output:
# 3

text = "programming"

count = 0

for char in text:
    if char in "aeiou":
        count += 1

print("Problem 1:", count)