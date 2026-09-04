# Count the frequency of every number in the array.

numbers = [1, 2, 2, 3, 1, 4, 2, 3]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)