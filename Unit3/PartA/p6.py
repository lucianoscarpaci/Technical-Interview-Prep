# Given a string post, use a queue to reverse the order of characters
# in each word within the sentence
from collections import deque

def edit_post(post):
    reversed_post = []
    for char in post:
        q = deque(post)
        q.reverse()
        q.appendleft(q.pop())
        q.rotate(-1)
        q = list(q)
    reversed_post.append(''.join(q))
    return ' '.join(reversed_post)

print(edit_post("this porsche"))
print(edit_post("is a beast"))
print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))