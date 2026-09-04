# Check whether the array contains any duplicate value.

numbers = [1, 2, 3, 4, 2]

seen = set()

has_duplicate = False

for number in numbers:
    if number in seen:
        has_duplicate = True
        break

    seen.add(number)

print(has_duplicate)