
# Print the binary tree using preorder traversal.
# Order: Root -> Left -> Right

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


def preorder(node):
    if node is None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)


preorder(root)