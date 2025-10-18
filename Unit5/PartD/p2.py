# Given the head of a singly linked list,
# reverse the list, and return the reversed list.
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
