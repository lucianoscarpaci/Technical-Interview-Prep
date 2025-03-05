from collections import deque

def clean_post(post):
    lowercase_queue = deque()
    uppercase_queue = deque()

    for char in post:
        if char.islower():
            lowercase_queue.append(char)
        elif char.isupper():
            uppercase_queue.append(char)
        # If the previous char in stack was lowercase remove it
            if lowercase_queue and lowercase_queue[-1] == char.lower():
                lowercase_queue.pop()
            else:
                uppercase_queue.append(char)
    result = ''.join(uppercase_queue) + ''.join(lowercase_queue)
    return result

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s"))