from collections import deque


class Puff:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right


def print_design(design):
    if not design:
        return []
    queue = deque([design])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(result)


"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff(
    "Vanilla", Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), Puff("Strawberry")
)
print_design(croquembouche)
