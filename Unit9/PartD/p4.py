class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


from collections import deque


# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root


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


def flatten_orders(orders):
    def preorder(node):
        if not node:
            return None

        # Recursively flatten the left and right subtrees
        left_tail = preorder(node.left)
        right_tail = preorder(node.right)

        # If there was a left subtree, rewire the pointers
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        # The new tail is the right_tail if it exists, otherwise the left_tail, otherwise the node itself
        if right_tail:
            return right_tail
        if left_tail:
            return left_tail
        return node

    preorder(orders)
    return orders


"""
        Croissant
       /         \
    Cupcake      Bagel
   /      \           \
Cake     Pie         Blondies
"""
# Using build_tree() function included at the top of page
items = ["Croissant", "Cupcake", "Bagel", "Cake", "Pie", None, "Blondies"]
orders = build_tree(items)

# Using print_tree() function included at the top of page
print_tree(flatten_orders(orders))
