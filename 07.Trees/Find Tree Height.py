# Find the height of the binary tree using recursion.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)


def tree_height(node):
    if node is None:
        return 0

    left_height = tree_height(node.left)
    right_height = tree_height(node.right)

    return 1 + max(left_height, right_height)


print("Height:", tree_height(root))