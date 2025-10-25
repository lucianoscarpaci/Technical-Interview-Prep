class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


# Given the head of a linked list,
# return a list of the values in the linked list in the
# order they appear.
def traverse_linked_list(head):
    current = head
    values = []  # List to store the values
    while current:
        values.append(current.val)  # Collect the value
        current = current.next
    return values  # Return the list of values
