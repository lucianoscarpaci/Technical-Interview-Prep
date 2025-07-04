class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


def merge_playlists(playlist1, playlist2, a, b):
    prev_a = playlist1
    for _ in range(a - 1):
        prev_a = prev_a.next
    node_b = prev_a
    for _ in range(b - a + 2):
        node_b = node_b.next
    prev_a.next = playlist2
    current = playlist2
    while current.next:
        current = current.next
    current.next = node_b
    return playlist1


playlist1 = Node(
    ("Flea", "St. Vincent"),
    Node(
        ("Juice", "Lizzo"),
        Node(
            ("Tenderness", "Jay Som"),
            Node(("Ego Death", "The Internet"), Node(("Empty", "Kevin Abstract"))),
        ),
    ),
)

playlist2 = Node(("Dreams", "Solange"), Node(("First", "Gallant")))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))
