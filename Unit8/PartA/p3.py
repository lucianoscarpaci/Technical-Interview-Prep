class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_vine(root):
    if root is None:
        return []
    list = []
    list.append(root.val)
    if root.right:
        list.append(root.right.val)
        list.append(root.right.right.val)
    return list


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode(
    "Root",
    TreeNode("Node1", TreeNode("Leaf1")),
    TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")),
)

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
