# Delete a value from a Binary Search Tree.
import bst

def delete(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)

    elif value > root.value:
        root.right = delete(root.right, value)

    else:
        # Case 1: Node has no child.
        if root.left is None and root.right is None:
            return None

        # Case 2: Node has only a right child.
        if root.left is None:
            return root.right

        # Case 2: Node has only a left child.
        if root.right is None:
            return root.left

        # Case 3: Node has two children.
        successor = bst.find_min_node(root.right)

        root.value = successor.value

        root.right = delete(root.right, successor.value)

    return root