class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


"""
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

    Leaf nodes have an integer value.
    The root has a string value of either "+", "-", "*", or "/".

The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.
"""


def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    if root.val == "-":
        return root.left.val - root.right.val
    if root.val == "*":
        return root.left.val * root.right.val
    if root.val == "/":
        return root.left.val / root.right.val


apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

print(calculate_yield(apple_tree))
