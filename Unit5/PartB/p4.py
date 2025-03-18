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
Write a function halve_list() that accepts the head of a linked list whose values are 
integers and divides each value by two.
 Return the head of the modified list.
"""


def halve_list(head):
    current = head
    while current:
        current.value /= 2
        current = current.next

    return head


node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))
"""
2.5  -> 3 -> 3.5
"""
