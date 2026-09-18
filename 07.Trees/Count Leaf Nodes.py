# Count the number of leaf nodes in the binary tree.

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


def count_leaves(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    return count_leaves(node.left) + count_leaves(node.right)


print("Leaf nodes:", count_leaves(root))