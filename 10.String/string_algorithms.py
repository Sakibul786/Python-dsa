# Question 1:
# Check whether a string is a palindrome.
# Ignore uppercase/lowercase differences and non-alphanumeric characters.

def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("Madam"))
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("Python"))


# Question 2:
# Check whether two strings are anagrams.
# Ignore spaces and uppercase/lowercase differences.

from collections import Counter


def are_anagrams(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    return Counter(first) == Counter(second)


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))
print(are_anagrams("Dormitory", "Dirty room"))


# Question 3:
# Find the first index of a pattern in a text using naive pattern matching.
# Return -1 if the pattern does not exist.

def naive_search(text, pattern):
    if pattern == "":
        return 0

    for start in range(len(text) - len(pattern) + 1):
        if text[start:start + len(pattern)] == pattern:
            return start

    return -1


print(naive_search("python programming", "program"))
print(naive_search("hello world", "world"))
print(naive_search("hello", "xyz"))


# Question 4:
# Build the LPS (Longest Prefix Suffix) array for a pattern.

def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    index = 1

    while index < len(pattern):
        if pattern[index] == pattern[length]:
            length += 1
            lps[index] = length
            index += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[index] = 0
            index += 1

    return lps


print(build_lps("ABABAC"))
print(build_lps("AAAA"))


# Question 5:
# Implement KMP to find the first occurrence of a pattern in a text.
# Return -1 if the pattern does not exist.

def kmp_search(text, pattern):
    if pattern == "":
        return 0

    lps = build_lps(pattern)

    text_index = 0
    pattern_index = 0

    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                return text_index - pattern_index

        elif pattern_index > 0:
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1

    return -1


print(kmp_search("ABABDABACDABABCABAB", "ABABCABAB"))
print(kmp_search("python programming", "program"))
print(kmp_search("hello world", "xyz"))


# Question 6:
# Find every starting index where a pattern occurs in a text using KMP.

def kmp_find_all(text, pattern):
    if pattern == "":
        return list(range(len(text) + 1))

    lps = build_lps(pattern)

    text_index = 0
    pattern_index = 0
    matches = []

    while text_index < len(text):
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == len(pattern):
                matches.append(text_index - pattern_index)
                pattern_index = lps[pattern_index - 1]

        elif pattern_index > 0:
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1

    return matches


print(kmp_find_all("ABABABAB", "ABAB"))


# Question 7:
# State the time complexity of naive pattern matching and KMP.
#
# Answer:
# Naive pattern matching: O(N * M) worst case.
# KMP: O(N + M).
# N is the text length, and M is the pattern length.