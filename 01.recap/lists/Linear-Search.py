# Problem 5:
# Given a list and a target number, search for the target.
#
# Do NOT use:
#   in
#
# If the target exists, print "Found".
# Otherwise, print "Not Found".
#
# Example:
# numbers = [10, 25, 30, 45, 60]
# target = 45
#
# Expected Output:
# Found


numbers = [10, 25, 30, 45, 60]
target = 45

found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Problem 5: Found")
else:
    print("Problem 5: Not Found")