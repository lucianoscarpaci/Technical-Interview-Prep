class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(node):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("None")
    # Remove trailing "None" values that represent missing nodes at the end of the tree
    while result and result[-1] == "None":
        result.pop()
    return result


def insert_into_bst(root, val):
    if val < root.val:
        if root.left:
            insert_into_bst(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_into_bst(root.right, val)
        else:
            root.right = TreeNode(val)


def bst_from_preorder(preorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    for val in preorder[1:]:
        insert_into_bst(root, val)
    return root


preorder = [8, 5, 1, 7, 10, 12]
root = bst_from_preorder(preorder)
print("Preorder:", root)
