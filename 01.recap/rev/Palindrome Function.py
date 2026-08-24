# Problem 4:
# Create a function named is_palindrome(text)
# that returns True if the string is a palindrome,
# otherwise False.
#
# Do NOT use [::-1].
#
# Example:
# text = "madam"
#
# Expected Output:
# True
#
# Example:
# text = "python"
#
# Expected Output:
# False

def is_palindrome(text):

    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text


print("Problem 4:", is_palindrome("madam"))
print("Problem 4:", is_palindrome("python"))