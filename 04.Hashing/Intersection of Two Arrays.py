# Find the common elements between two arrays.

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 4, 5, 6, 7]

set1 = set(numbers1)

intersection = []

for number in numbers2:
    if number in set1:
        intersection.append(number)

print(intersection)