class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def survey_tree(root):
    current = root
    result = []
    if not current:
      return []

    left_tree = survey_tree(current.left)
    right_tree = survey_tree(current.right)

    return left_tree + right_tree + [current.val]


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

print(survey_tree(magnolia))
