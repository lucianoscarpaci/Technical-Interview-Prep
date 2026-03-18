# Understand & Plan & Implement
# Use stack
# Question is similar to the valid parenthesis
# we need to add or remove nfts if they are matching
# My guess is if we have an 1 add, and 2 removes then make it balanced ? so its add and remove
# make all adds and removes balanced by using queue ?
# If the adds and removes are balanced return true
# Otherwise return False
def validate_nft_actions(actions):
    stack = []
    for action in actions:
        if action == "add":
            stack.append(action)
        elif action == "remove":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))
"""
True
True
False
"""
