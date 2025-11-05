class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root):
    def depth(node):
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        return max(left_depth, right_depth) + 1

    def diameter_helper(node):
        nonlocal diameter
        if not node:
            return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        diameter = max(diameter, left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    diameter = 0
    diameter_helper(root)
    return diameter

# Helper function to build a tree from a list (for testing)
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# Example usage:
root_list = [1,2,3,4,5]
root = build_tree(root_list)
print(diameter_of_binary_tree(root))
