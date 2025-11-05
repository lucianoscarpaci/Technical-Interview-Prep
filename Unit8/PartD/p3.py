class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def get_decision(root):
    if root.val == "AND":
        return get_decision(root.left) and get_decision(root.right)
    elif root.val == "OR":
        return get_decision(root.left) or get_decision(root.right)
    else:
        return root.val

"""
        OR
      /    \
    True  False
"""
expression1 = TreeNode("OR", TreeNode(True), TreeNode(False))

"""
       False
"""
expression2 = TreeNode(False)

print(get_decision(expression1))
print(get_decision(expression2))
