# Check whether the brackets in the string are valid and balanced.

text = "({[]})"

stack = []

pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

for character in text:
    if character in "([{":
        stack.append(character)

    elif character in ")]}":
        if not stack or stack[-1] != pairs[character]:
            print(False)
            break

        stack.pop()

else:
    print(len(stack) == 0)