# Calculate the sum of all values in the binary tree.

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


def tree_sum(node):
    if node is None:
        return 0

    return (
        node.data
        + tree_sum(node.left)
        + tree_sum(node.right)
    )


print("Sum:", tree_sum(root))