from collections import deque


class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key  # Plant price
        self.val = val  # Plant name
        self.left = left
        self.right = right


def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


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


def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(key, value)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_key, left_value)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_key, right_value)
            queue.append(node.right)
        index += 1

    return root


def remove_plant(collection, name):
    if collection is None:
        return None

    if name < collection.val:
        collection.left = remove_plant(collection.left, name)
    elif name > collection.val:
        collection.right = remove_plant(collection.right, name)
    else:
        if collection.left is None and collection.right is None:
            return None

        if collection.left is None:
            return collection.right
        elif collection.right is None:
            return collection.left
        predessor = max_value_node(collection.left)
        collection.val = predessor.val
        collection.left = remove_plant(collection.left, predessor.val)
    return collection


"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))
