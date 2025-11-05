class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mystery(root):
    if not root:
        return []
    return [root.val] + mystery(root.left) + mystery(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(mystery(root))  # Output: [1, 2, 4, 5, 3]