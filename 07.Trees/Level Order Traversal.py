# Print the binary tree using level-order traversal.

from collections import deque


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
root.right.right = TreeNode(60)


queue = deque([root])

while queue:
    current = queue.popleft()

    print(current.data)

    if current.left:
        queue.append(current.left)

    if current.right:
        queue.append(current.right)