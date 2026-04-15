from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_tree(root):
    if not root:
        return 0
    # Level order traversal using a queue
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(root.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return level


root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")
print_tree(root)
