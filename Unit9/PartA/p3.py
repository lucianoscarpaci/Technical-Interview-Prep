from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
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


def max_tiers(cake):
    if cake is None:
        return 0
    
    queue = deque([cake])
    max_tiers = 0
    # BFS
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        max_tiers += 1
    return max_tiers


"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = [
    "Chocolate",
    "Vanilla",
    "Strawberry",
    None,
    None,
    "Chocolate",
    "Coffee",
]
cake = build_tree(cake_sections)

print(max_tiers(cake))
