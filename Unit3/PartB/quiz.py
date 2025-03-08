def check_balanced(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if not stack or stack.pop() != matching_parentheses[char]:
                return False
    return not stack


print(check_balanced('([])'))
print(check_balanced('([)]'))

