# Binary Search Tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Question 1: Insert a value into a Binary Search Tree.
def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


# Question 2: Search for a target value in a Binary Search Tree.
def search(root, target):
    if root is None:
        return False

    if root.value == target:
        return True

    if target < root.value:
        return search(root.left, target)

    return search(root.right, target)


# Question 3: Find the minimum value in a Binary Search Tree.
def find_min(root):
    if root is None:
        return None

    current = root

    while current.left is not None:
        current = current.left

    return current.value


# Question 4: Find the maximum value in a Binary Search Tree.
def find_max(root):
    if root is None:
        return None

    current = root

    while current.right is not None:
        current = current.right

    return current.value


# Question 5: Perform inorder traversal of a Binary Search Tree.
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Search 60:", search(root, 60))
print("Search 90:", search(root, 90))
print("Minimum:", find_min(root))
print("Maximum:", find_max(root))

print("Inorder traversal:", end=" ")
inorder(root)
print()