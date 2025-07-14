class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def sum_inventory(inventory):
    current = inventory
    if current is None:
        return 0
    sum_left = sum_inventory(current.left)
    sum_right = sum_inventory(current.right)

    return current.val + sum_left + sum_right


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
