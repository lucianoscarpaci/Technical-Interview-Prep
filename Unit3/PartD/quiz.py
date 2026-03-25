# What is output of code snippet?
from collections import deque


def check_balances(s):
    stack = []
    matches = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in matches.values():
            stack.append(char)

        if char in matches.keys():  # Check if char is a closing bracket
            if not stack or stack[-1] != matches[char]:
                return False  # Return False if not balanced
            stack.pop()  # Pop only if the top of the stack matches

    return not stack
