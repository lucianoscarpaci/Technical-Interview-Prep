class SinglyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

# count_nodes_with_value() accepts
# head of a singly linked list and a value
# and returns the number of nodes in the list
# with value value equal to target.
def count_nodes_with_value(head, target):
    if head is None:  # Check if the head is None
        return 0
    count = 0
    current = head
    while current:
        if current.data == target:
            count += 1
        current = current.next
    return count