class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def survey_tree(root):
    current = root
    if current is None:
        return []

    left_subtree = survey_tree(current.left)
    right_subtree = survey_tree(current.right)

    return left_subtree + right_subtree + [current.val]


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
