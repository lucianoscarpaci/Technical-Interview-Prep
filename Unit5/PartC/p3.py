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
    # Use a temp node to simplify head operations
    temp = Node(0)
    temp.next = head

    # `prev` is the last node before the current sequence of duplicates or unique values
    prev = temp
    current = head

    while current:
        # Move current to skip over all duplicates
        while current.next and current.value == current.next.value:
            current = current.next

        # If `prev.next` is `current`, no duplicates were found between `prev` and `current`
        if prev.next == current:
            prev = prev.next
        else:
            # Otherwise, skip all duplicates
            prev.next = current.next

        # Move current to the next distinct value
        current = current.next

    return temp.next


head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))
