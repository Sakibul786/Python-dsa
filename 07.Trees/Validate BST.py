# Check whether a Binary Tree is a valid Binary Search Tree.

def is_valid_bst(root, minimum=float("-inf"), maximum=float("inf")):
    if root is None:
        return True

    if root.value <= minimum or root.value >= maximum:
        return False

    return (
        is_valid_bst(root.left, minimum, root.value)
        and is_valid_bst(root.right, root.value, maximum)
    )