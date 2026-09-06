# Reverse the given string using a stack.

text = "hello"

stack = []

for character in text:
    stack.append(character)

reversed_text = ""

while stack:
    reversed_text += stack.pop()

print(reversed_text)