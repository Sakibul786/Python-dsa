# Problem 2:
# Reverse a given string.
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

text = "python"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Problem 2:", reversed_text)