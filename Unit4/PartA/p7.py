# Add NFTs in a balanced way. For every "add" action must be properly closed by a corresponding
# "remove" action. The "add" action must be performed before the "remove" action.
# Write the validate_nft_actions(0 function which takes a list of actions either "add" or "remove"
# and returns True if the actions are balanced and False otherwise.
# I will use a stack to keep track of the actions. If the stack is empty, I will add the action to the stack.
# If the stack is not empty, I will check if the action is the opposite of the top of the stack. If it is, I will
def validate_nft_actions():
    stack = []
    for action in actions:
        if action == "add":
            stack.append(action) # This will be stack = ["add"]
        elif action == "remove":
            if stack and stack[-1] == "add":
                stack.pop()

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions)) #True
print(validate_nft_actions(actions_2)) #True
print(validate_nft_actions(actions_3)) #False
