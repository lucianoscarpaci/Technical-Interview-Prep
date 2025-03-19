class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


shy_guy = Node("Shy Guy")
link = Node("Link")
diddy_kong = Node("Diddy Kong")
toad = Node("Toad")
dry_bones = Node("Dry Bones")
link.next = diddy_kong
shy_guy.next = link
diddy_kong.next = toad
toad.next = dry_bones

# Add code to update the list here
print("Current List:")
print_linked_list(shy_guy)
"""
Current List:
Shy Guy -> Link -> Diddy Kong -> Toad -> Dry Bones
"""
