# Search for a target value in the binary tree.

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

target = 50


def search_tree(node, target):
    if node is None:
        return False

    if node.data == target:
        return True

    return (
        search_tree(node.left, target)
        or search_tree(node.right, target)
    )


print(search_tree(root, target))