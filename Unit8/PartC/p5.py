class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    current = root
    if not current:
        return 0
    if current.right is None and current.left is None:
        return current.val

    right_tree = calculate_yield(current.right)
    left_tree = calculate_yield(current.left)

    if current.val == '+':
        return left_tree + right_tree
    if current.val == '-':
        return left_tree - right_tree
    if current.val == '*':
        return left_tree * right_tree
    if current.val == '/':
        return left_tree / right_tree
 
"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
