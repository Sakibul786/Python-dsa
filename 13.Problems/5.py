"""
PROBLEM:

You are given two words: begin_word and end_word,
and a list of allowed words.

Transform begin_word into end_word by changing exactly
one character at a time.

Every intermediate word must exist in the given word list.

Return the number of words in the shortest transformation
sequence.

If no transformation is possible, return 0.

EXAMPLE:

begin_word = "hit"
end_word = "cog"

word_list = [
    "hot",
    "dot",
    "dog",
    "lot",
    "log",
    "cog"
]

Expected Output:
5

One shortest sequence:
hit -> hot -> dot -> dog -> cog


APPROACH:

Use Breadth-First Search (BFS).

1. Put the starting word into a queue.
2. Generate all possible words by changing one character.
3. Check whether each generated word exists in the word list.
4. Add valid, unvisited words to the queue.
5. Track the number of transformations.
6. Return the distance when the target word is reached.

BFS guarantees the shortest path in an unweighted graph.
"""

from collections import deque
import string


def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)

    if end_word not in word_set:
        return 0

    if begin_word == end_word:
        return 1

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        current_word, steps = queue.popleft()

        for index in range(len(current_word)):
            for char in string.ascii_lowercase:

                if char == current_word[index]:
                    continue

                next_word = (
                    current_word[:index]
                    + char
                    + current_word[index + 1:]
                )

                if next_word == end_word:
                    return steps + 1

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0


# Test Case 1
begin_word = "hit"
end_word = "cog"

word_list = [
    "hot",
    "dot",
    "dog",
    "lot",
    "log",
    "cog"
]

print(word_ladder(begin_word, end_word, word_list))



# Test Case 2: No valid transformation
begin_word = "hit"
end_word = "cog"

word_list = ["hot", "dot", "dog", "lot", "log"]

print(word_ladder(begin_word, end_word, word_list))



# Test Case 3: Direct transformation
begin_word = "cat"
end_word = "bat"

word_list = ["bat", "hat", "rat"]

print(word_ladder(begin_word, end_word, word_list))



# Test Case 4: Same starting and ending word
print(word_ladder("cat", "cat", ["bat", "rat"]))



"""
EXPLANATION:

Starting word: hit

LEVEL 1:
hit

Change one character:
hot

LEVEL 2:
hot

Possible next words:
dot, lot

LEVEL 3:
dot, lot

From dot:
dog

From lot:
log

LEVEL 4:
dog, log

From dog:
cog

LEVEL 5:
cog

The shortest sequence contains 5 words.

WHY BFS?

BFS explores all words at the current transformation
distance before exploring the next distance.

Therefore, the first time we reach end_word,
we have found a shortest transformation sequence.

WHY USE A SET?

A set provides efficient membership checking.
It also prevents revisiting words.

COMPLEXITY:

Let:
N = Number of words in the word list
L = Length of each word
A = Number of possible characters (26)

Time Complexity:
O(N * L * A * L)

The extra L factor comes from constructing each
candidate word using string slicing and concatenation.

Space Complexity:
O(N * L)

The word set, visited set, and BFS queue
can store up to N words.

IMPORTANT:
All words must have the same length.
The standard Word Ladder problem assumes this condition.
"""