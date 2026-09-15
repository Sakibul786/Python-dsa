
# Print the binary tree using inorder traversal.
# Order: Left -> Root -> Right

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


def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data)
    inorder(node.right)


inorder(root)