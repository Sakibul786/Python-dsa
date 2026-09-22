#  Find the inorder successor of a given value in a BST.

from logging import root


def find_successor(root, value):
    successor = None

    while root is not None:
        if value < root.value:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor.value if successor else None


print(find_successor(root, 50))