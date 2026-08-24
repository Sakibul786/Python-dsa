# Problem 5:
# Create a recursive function to reverse a string.
#
# Do NOT use:
# [::-1]
#
# Example:
# text = "python"
#
# Expected Output:
# nohtyp

def reverse_string(text):

    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print(reverse_string("python"))