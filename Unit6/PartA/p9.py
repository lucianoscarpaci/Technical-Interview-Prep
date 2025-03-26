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


def selective_trail_clearing(trailhead, m, n):
    # Write a function to traverse the trail and remove every nth marker
    current = trailhead
    while current:
        # Skip m-1 markers
        for _ in range(m - 1):
            if current:
                current = current.next
            else:
                return trailhead

        for _ in range(n):
            if current and current.next:
                current.next = current.next.next
            else:
                return trailhead
        current = current.next

    return trailhead


trailhead = Node(
    1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10)))))))))
)
print_linked_list(selective_trail_clearing(trailhead, 2, 3))
