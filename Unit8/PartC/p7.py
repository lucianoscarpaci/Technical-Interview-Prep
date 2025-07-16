class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    if root is None:
        return 0
    if root.val > threshold:
        return 1
    left_tree = count_old_growth(root.left, threshold)
    right_tree = count_old_growth(root.right, threshold)

    return 1 + left_tree + right_tree

"""
     100
     /  \
    /    \
  1200  1500
  /     /  \
20    700  2600
"""

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))
