from collections import deque


# Tree Node class
class Puff:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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
    root = Puff(value)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_value = get_value(values[index])
            node.left = Puff(left_value)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_value = get_value(values[index])
            node.right = Puff(right_value)
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


def listify_design(design):
    current = design
    if current is None:
        return []
    result = []
    queue = deque([current])
    while queue:
        level = []
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


croquembouche = Puff(
    "Vanilla", Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), Puff("Strawberry")
)
print(listify_design(croquembouche))
