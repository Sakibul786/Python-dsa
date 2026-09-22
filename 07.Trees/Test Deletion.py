# Build a BST and delete different types of nodes.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def find_min_node(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


def delete(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)

    elif value > root.value:
        root.right = delete(root.right, value)

    else:
        if root.left is None and root.right is None:
            return None

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        successor = find_min_node(root.right)

        root.value = successor.value
        root.right = delete(root.right, successor.value)

    return root


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

print("Before deletion:")
inorder(root)

root = delete(root, 20)

print("\nAfter deleting 20:")
inorder(root)

root = delete(root, 30)

print("\nAfter deleting 30:")
inorder(root)

root = delete(root, 50)

print("\nAfter deleting 50:")
inorder(root)