from collections import deque


class TreeNode:
    def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    def get_value(item):
        if isinstance(item, tuple):
            return item[1]
        else:
            return item

    value = get_value(values[0])
    root = TreeNode(value)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_value = get_value(values[index])
            node.left = TreeNode(left_value)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_value = get_value(values[index])
            node.right = TreeNode(right_value)
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


def larger_order_tree(order_tree, order):
    if order_tree is None:
        return None
    queue = deque([order_tree])
    while queue:
        node = queue.popleft()
        if node.val == order:
            if node.left:
                return node.left
            if node.right:
                return node.right
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            return None


"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

