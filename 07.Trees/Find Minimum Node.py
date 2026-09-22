#Find the node with the minimum value in a subtree.

def find_min_node(root):
    current = root

    while current.left is not None:
        current = current.left

    return current