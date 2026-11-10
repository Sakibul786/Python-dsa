"""
PROBLEM:

Given an integer array nums, find the length of the
longest strictly increasing subsequence.

A subsequence is a sequence that can be obtained by
removing some elements without changing the order
of the remaining elements.

EXAMPLE:

nums = [10, 9, 2, 5, 3, 7, 101, 18]

Expected Output:
4

Explanation:
One longest increasing subsequence is:

[2, 3, 7, 18]

Its length is 4.


APPROACH:

Use Dynamic Programming with Binary Search.

1. Create an empty list called tails.
2. Traverse every number in the array.
3. Find the first position in tails where the value
   is greater than or equal to the current number.
4. Replace that value with the current number.
5. If no such position exists, append the current number.
6. The length of tails is the LIS length.

"""


from bisect import bisect_left


def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    tails = []

    for num in nums:
        position = bisect_left(tails, num)

        if position == len(tails):
            tails.append(num)
        else:
            tails[position] = num

    return len(tails)


# Test Case 1
nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(longest_increasing_subsequence(nums))



# Test Case 2
nums = [0, 1, 0, 3, 2, 3]

print(longest_increasing_subsequence(nums))



# Test Case 3
nums = [7, 7, 7, 7, 7]

print(longest_increasing_subsequence(nums))



# Test Case 4
nums = [1, 2, 3, 4, 5]

print(longest_increasing_subsequence(nums))



# Test Case 5
nums = [5, 4, 3, 2, 1]

print(longest_increasing_subsequence(nums))



# Test Case 6
nums = []

print(longest_increasing_subsequence(nums))



"""
DRY RUN:

nums = [10, 9, 2, 5, 3, 7, 101, 18]

Initially:
tails = []

Step 1:
Number = 10
tails = [10]

Step 2:
Number = 9
Replace 10 with 9.
tails = [9]

Step 3:
Number = 2
Replace 9 with 2.
tails = [2]

Step 4:
Number = 5
Append 5.
tails = [2, 5]

Step 5:
Number = 3
Replace 5 with 3.
tails = [2, 3]

Step 6:
Number = 7
Append 7.
tails = [2, 3, 7]

Step 7:
Number = 101
Append 101.
tails = [2, 3, 7, 101]

Step 8:
Number = 18
Replace 101 with 18.
tails = [2, 3, 7, 18]

Final Answer:
4


IMPORTANT:

The tails list does not necessarily represent
the actual LIS subsequence.

It stores the smallest possible ending values
for increasing subsequences of different lengths.

We only need its length to calculate the LIS length.

WHY USE BINARY SEARCH?

A normal DP solution takes O(N^2) time.

Binary search helps find the replacement position
in O(log N) time.

COMPLEXITY:

N = Number of elements in the array.

Time Complexity:
O(N log N)

Space Complexity:
O(N)


INTERVIEW FOLLOW-UP:

How would you return the actual LIS elements,
not just their length?

Hint:
Use parent indices and track the index of each
element's predecessor.
"""