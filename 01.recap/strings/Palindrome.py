# Problem 3:
# Check whether a string is a palindrome.
#
# A palindrome reads the same forward and backward.
#
# Example:
# text = "madam"
#
# Expected Output:
# Palindrome

text = "madam"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("Problem 3: Palindrome")
else:
    print("Problem 3: Not Palindrome")