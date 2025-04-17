from collections import deque


class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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


def can_rearrange_orders(order1, order2):
    # Base case
    if not order1 and not order2:
        return True
    if not order1 or not order2:
        return False
    if order1.val != order2.val:
        return False
    # Recursively check left and right subtrees
    return (
        (can_rearrange_orders(order1.left, order2.left) and can_rearrange_orders(order1.right, order2.right))
        or (can_rearrange_orders(order1.left, order2.right) and can_rearrange_orders(order1.right, order2.left))
    )


"""
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon                   Lemon            Vanilla
        /      \        /   \                  /     \           /      \
      Ube    Almond  Chai   Carrot       Carrot      Chai    Almond    Ube 
                     /   \        \       /          /   \      
                 Chai   Maple   Smore   Smore    Maple   Chai
"""

# Using build_tree() function included at top of page
flavors1 = [
    "Red Velvet",
    "Vanilla",
    "Lemon",
    "Ube",
    "Almond",
    "Chai",
    "Carrot",
    None,
    None,
    None,
    None,
    "Chai",
    "Maple",
    None,
    "Smore",
]
flavors2 = [
    "Red Velvet",
    "Lemon",
    "Vanilla",
    "Carrot",
    "Chai",
    "Almond",
    "Ube",
    "Smore",
    None,
    "Maple",
    "Chai",
]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

print(can_rearrange_orders(order1, order2))
