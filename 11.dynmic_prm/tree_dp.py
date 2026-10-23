
# Question 1:
# Define a binary tree node.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Question 2:
# Find the diameter of a binary tree.
# The diameter is measured in number of edges.

def tree_diameter(root):
    diameter = 0

    def depth(node):
        nonlocal diameter

        if node is None:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        diameter = max(
            diameter,
            left_depth + right_depth
        )

        return 1 + max(left_depth, right_depth)

    depth(root)
    return diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print("Tree diameter:", tree_diameter(root))


# Question 3:
# Find the maximum path sum in a binary tree.

def max_path_sum(root):
    best_sum = float("-inf")

    def max_gain(node):
        nonlocal best_sum

        if node is None:
            return 0

        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))

        current_path = (
            node.value + left_gain + right_gain
        )

        best_sum = max(best_sum, current_path)

        return node.value + max(left_gain, right_gain)

    max_gain(root)
    return best_sum


root_sum = TreeNode(-10)
root_sum.left = TreeNode(9)
root_sum.right = TreeNode(20)
root_sum.right.left = TreeNode(15)
root_sum.right.right = TreeNode(7)

print("Maximum path sum:", max_path_sum(root_sum))


# Question 4:
# Find the maximum sum of non-adjacent tree nodes.
# If a node is selected, its direct children cannot be selected.

def maximum_independent_set(root):
    def solve(node):
        if node is None:
            return 0, 0

        left_skip, left_take = solve(node.left)
        right_skip, right_take = solve(node.right)

        take = (
            node.value
            + left_skip
            + right_skip
        )

        skip = (
            max(left_skip, left_take)
            + max(right_skip, right_take)
        )

        return skip, take

    skip, take = solve(root)
    return max(skip, take)


root_set = TreeNode(10)
root_set.left = TreeNode(1)
root_set.right = TreeNode(2)
root_set.left.left = TreeNode(4)
root_set.left.right = TreeNode(5)
root_set.right.right = TreeNode(3)

print(
    "Maximum independent set sum:",
    maximum_independent_set(root_set)
)


# Question 5:
# Count the number of nodes in a binary tree.

def count_nodes(root):
    if root is None:
        return 0

    return (
        1
        + count_nodes(root.left)
        + count_nodes(root.right)
    )


print("Number of nodes:", count_nodes(root))


# Question 6:
# State the time and auxiliary space complexities.
#
# Answer:
# Tree Diameter:
# Time: O(n)
# Auxiliary space: O(h)
#
# Maximum Path Sum:
# Time: O(n)
# Auxiliary space: O(h)
#
# Maximum Independent Set:
# Time: O(n)
# Auxiliary space: O(h)
#
# Node Count:
# Time: O(n)
# Auxiliary space: O(h)
#
# Here, n is the number of nodes and h is the tree height.
# The auxiliary space includes the recursive call stack.
