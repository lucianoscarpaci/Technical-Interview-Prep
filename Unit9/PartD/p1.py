from collections import deque


class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


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


def build_cookie_tree(descriptions):
    child_nodes = set()
    node_map = {}

    for parent, child, is_left in descriptions:
        if parent not in node_map:
            node_map[parent] = TreeNode(parent)
        if child not in node_map:
            node_map[child] = TreeNode(child)
        if is_left == 1:
            node_map[parent].left = node_map[child]
        else:
            node_map[parent].right = node_map[child]

    child_nodes.add(child)
    root = None

    for node_val in node_map:
        if node_val not in child_nodes:
            root = node_map[node_val]
            break
    return root


descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1],
]

descriptions2 = [["Ginger Snap", "Snickerdoodle", 0], ["Ginger Snap", "Shortbread", 1]]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
