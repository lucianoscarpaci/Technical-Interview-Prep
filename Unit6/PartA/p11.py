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


def merge_trail(trailhead):
    if not trailhead:
        return None

    new_node = Node(0)
    tail = new_node
    current = trailhead.next
    segment = 0

    while current:
        if current.value == 0:
            if segment > 0:
                tail.next = Node(segment)
                tail = tail.next
            segment = 0
        else:
            segment += current.value
        current = current.next
    return new_node.next


trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(4, Node(2, Node(0)))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1))
print_linked_list(merge_trail(trail2))
