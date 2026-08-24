# Problem 2:
# Create a function named char_frequency(text)
# that returns the frequency of every character.
#
# Example:
# text = "banana"
#
# Expected Output:
# {'b': 1, 'a': 3, 'n': 2}


def char_frequency(text):

    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


text = "banana"

print("Problem 2:", char_frequency(text))