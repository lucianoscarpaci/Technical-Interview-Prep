class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def remove_duplicate_markers(trailhead):
    current = trailhead
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next

    return trailhead


trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))

print_linked_list(remove_duplicate_markers(trailhead))
