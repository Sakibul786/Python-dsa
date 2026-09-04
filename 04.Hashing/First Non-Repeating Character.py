# Find the first character that appears only once.

text = "swiss"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

for character in text:
    if frequency[character] == 1:
        print(character)
        break