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


def delete_dupes(head):
    temp_head = Node("temp")  # Initialize a temporary head node
    temp_head.next = head  # Point the temporary head at the input list

    # Traverse the list
    previous = temp_head
    current = head
    while current:
        if current.value == previous.value:  # If the current node is the node to delete
            previous.next = current.next  # Delete the node
            break  # Break out of the loop

        previous = current
        current = current.next
    return temp_head.next


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
