# Question 1:
# Implement a Trie with insert(), search(), and starts_with().

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True


trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("care")
trie.insert("dog")

print(trie.search("cat"))
print(trie.search("cab"))
print(trie.starts_with("ca"))
print(trie.search("car"))


# Question 2:
# Count how many complete words are stored in the Trie.

def count_words(node):
    count = 1 if node.is_end else 0

    for child in node.children.values():
        count += count_words(child)

    return count


print("Word count:", count_words(trie.root))


# Question 3:
# Return all words stored in the Trie.

def get_all_words(node, prefix=""):
    words = []

    if node.is_end:
        words.append(prefix)

    for char, child in node.children.items():
        words.extend(get_all_words(child, prefix + char))

    return words


print("All words:", sorted(get_all_words(trie.root)))


# Question 4:
# Find all stored words that begin with a given prefix.

def words_with_prefix(trie, prefix):
    node = trie.root

    for char in prefix:
        if char not in node.children:
            return []

        node = node.children[char]

    return sorted(get_all_words(node, prefix))


print("Words with prefix 'ca':", words_with_prefix(trie, "ca"))
print("Words with prefix 'do':", words_with_prefix(trie, "do"))
print("Words with prefix 'xy':", words_with_prefix(trie, "xy"))


# Question 5:
# Explain why search("car") and starts_with("car") can return
# different results.
#
# Answer:
# search() checks whether the complete word exists.
# starts_with() checks only whether the character path exists.
# For example, if only "care" is inserted:
# search("car") returns False.
# starts_with("car") returns True.


# Question 6:
# What is the time complexity of inserting or searching a word?
#
# Answer:
# O(L), where L is the length of the word.
# Each character is processed once.


# Question 7:
# Insert "apple" and check "app" as a complete word and as a prefix.

trie2 = Trie()
trie2.insert("apple")

print(trie2.search("app"))
print(trie2.starts_with("app"))

trie2.insert("app")

print(trie2.search("app"))