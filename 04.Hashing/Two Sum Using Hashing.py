# Find two indices whose values add up to the target.

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for index, number in enumerate(numbers):
    complement = target - number

    if complement in seen:
        print([seen[complement], index])
        break

    seen[number] = index