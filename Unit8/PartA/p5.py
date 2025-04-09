class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


"""
You've grown an oak tree from a tiny little acorn and it's finally sprouting leaves! 
Given the root of a binary tree representing your oak tree, count the number of leaf nodes in the tree. 
A leaf node is a node that does not have any children.
Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""


def count_leaves(root):
    if root is None:
        return 0
    if (root.left and root.right) is None:
        return 1

    # recursively find left side and right side
    left_side = count_leaves(root.left)
    right_side = count_leaves(root.right)
    return left_side + right_side


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


print(count_leaves(oak1))
print(count_leaves(oak2))
