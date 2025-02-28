# reverse the order of comments before displaying them.
# For example, if the comments are ["Great post!", "Love it!", "Thanks for sharing."],
# the output should be ["Thanks for sharing.", "Love it!", "Great post!"].
# Comments are a list of strings. 
def reverse_comments_queue(comments):
  stack = []
  # Iterate through the comments
  for comment in comments:
    stack.append(comment) # stack = ['Great post!', 'Love it!', 'Thanks for sharing.']
    stack.reverse()
  return stack

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
