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


"""
Write a function delete_tail() that accepts the head of a linked list and 
removes the last node in the list. Return the head of the modified list.
Note: The "tail" of a list is the last element in the linked list. 
It is equivalent to lst[-1] in a normal list.
"""


def delete_tail(head):
    # If the list is empty or has only one element, return None or head
    if not head or not head.next:
        return None

    current = head
    # Traverse the list until the second last node
    while current.next.next:
        current = current.next

    # Remove the tail by setting the second last node's next to None
    current.next = None
    return head


# Create the nodes
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
# Link the nodes together
butterfly.next = ladybug
ladybug.next = beetle
# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))
"""
Common Butterfly -> Ladybug
"""
