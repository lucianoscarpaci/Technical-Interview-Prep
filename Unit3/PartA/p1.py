# You are managing a social media platform and need to ensure that post are formatted.
# () represent mentions, [] represent hashtags, {} represent links.
# A post is valid if every opening tag has a closing tag of same type.
# Tags are closed in correct order.
def is_valid_post_format(posts):
  # Iterate through the posts
    stack = []
    for post in posts: #post '(' #post ')'
        # if its an opening tag, push it to the stack
        if post in ["(", "[", "{"]: # True
            stack.append(post) # stack = ['(']
            # If its a closing tag, check the stack if the stack
            # is not empty and whether the tag at the top of the stack
            # is the corresponding opening tag
        else:
            if not stack:
                return False
            if post == ")" and stack[-1] != "(":
                return False
            if post == "]" and stack[-1] != "[":
                return False # stack = ['(]']
            if post == "}" and stack[-1] != "{":
                return False
            stack.pop() # stack = []
    return True #posts = "()"

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
