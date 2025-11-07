from collections import defaultdict
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


def most_popular_cookie_combo(root):
    max_count = 0
    cookie_combo = defaultdict(int)

    def traverse(root):
        nonlocal max_count
        if not root:
            return 0
        left_combo = traverse(root.left)
        right_combo = traverse(root.right)
        total_combo = root.val + left_combo + right_combo
        cookie_combo[total_combo] += 1
        max_count = max(cookie_combo[total_combo], max_count)
        return total_combo

    traverse(root)
    ans = []
    for key, cnt in cookie_combo.items():
        if cnt == max_count:
            ans.append(key)
    return ans


"""
       5
      / \
     2  -3
"""
cookies1 = TreeNode(5, TreeNode(2), TreeNode(-3))

"""
       5
      / \
     2  -5
"""
cookies2 = TreeNode(5, TreeNode(2), TreeNode(-5))

print(most_popular_cookie_combo(cookies1))
print(most_popular_cookie_combo(cookies2))
