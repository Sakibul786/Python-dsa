# Problem 5:
# Given a string, find the first character that
# does not repeat.
#
# Example:
# text = "aabbcdd"
#
# Expected Output:
# c

text = "aabbcdd"

frequency = {}

# Step 1: Count frequency
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Step 2: Find first character with frequency 1
for char in text:
    if frequency[char] == 1:
        print("Problem 5:", char)
        break