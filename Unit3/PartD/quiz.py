def is_valid_post_format(posts):
    parenthesis = []
    chars = {"(": ")", "[": "]", "{": "}"}
    for char in posts:
        if char in chars.keys():
            parenthesis.append(char)
        else:
            if parenthesis:
                last_open = parenthesis.pop()
                if chars[last_open] != char:
                    return False
    return True


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
#[(] char = ), last_open = ( 
print(is_valid_post_format("(]"))
