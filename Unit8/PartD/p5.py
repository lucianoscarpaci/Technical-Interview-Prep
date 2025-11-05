def flatten(root):
    if not root:
        return None

    stack = [root]
    prev = None

    while stack:
        current = stack.pop()

        if prev:
            prev.right = current
            prev.left = None

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        prev = current

    return root