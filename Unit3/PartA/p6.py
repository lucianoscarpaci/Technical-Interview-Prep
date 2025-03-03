# Given a string post, use a queue to reverse the order of characters
# in each word within the sentence
from collections import deque

def edit_post(post):
    q = deque(post)
    current_word = deque()
    reversed_post = []

    for char in q:
        if char != ' ':  # Continue reversing if not a space
            current_word.appendleft(char) # add char to the left of the current word
        else:
            # When a space is detected, finalize the current word
            reversed_post.append(''.join(current_word))
            reversed_post.append(' ')  # Add the space back
            current_word.clear() # clear the current word
    reversed_post.append(''.join(current_word)) # add the last word
    return ''.join(reversed_post)

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog"))