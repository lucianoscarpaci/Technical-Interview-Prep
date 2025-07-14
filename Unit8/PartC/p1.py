class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def right_vine(root):
    # Initialize an empty list to store the result.
    result = []
    # Set the current node to root
    current = root
    while current is not None:
        result.append(current.val)
        if current.right:
            current = current.right
        else:
            break
    return result


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
