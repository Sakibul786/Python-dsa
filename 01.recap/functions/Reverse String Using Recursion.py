# Problem 4:
# Create a recursive function to reverse a string.
#
# Do NOT use:
#   [::-1]
#   reversed()
#
# Example:
# text = "python"
#
# Expected Output:
# "nohtyp"

def reverse_string(text):

    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


text = "python"

print("Problem 4:", reverse_string(text))