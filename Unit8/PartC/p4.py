class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def sum_inventory(inventory):
    current = inventory
    if not current:
        return 0
    
    left_tree = sum_inventory(current.left)
    right_tree = sum_inventory(current.right)

    return current.val + left_tree + right_tree




"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(
    40, TreeNode(5, TreeNode(20)), TreeNode(10, TreeNode(1), TreeNode(30))
)

print(sum_inventory(inventory))
