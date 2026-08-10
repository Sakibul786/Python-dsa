# Problem 4:
# Given a string, count how many times each character appears.
#
# Example:
# text = "banana"
#
# Expected Output:
# b → 1
# a → 3
# n → 2

text = "banana"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Problem 4:", frequency)