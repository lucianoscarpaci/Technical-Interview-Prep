from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

root = TreeNode("Poseidon")
root.left = TreeNode("Atlantis")
root.right = TreeNode("Oceania")
root.left.left = TreeNode("Coral")
root.left.right = TreeNode("Pearl")
root.right.left = TreeNode("Kelp")
root.right.right = TreeNode("Reef")

# Using print_tree() included at the top of this page
print_tree(root)

