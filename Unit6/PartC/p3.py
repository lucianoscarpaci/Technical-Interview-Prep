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


def shuffle_playlist(playlist):
    if not playlist or not playlist.next:
        return playlist

    slow, fast = playlist, playlist
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, current = None, slow.next
    slow.next = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    first, second = playlist, prev
    while second:
        next_first, next_second = first.next, second.next
        first.next = second
        second.next = next_first
        second = next_second
    return playlist


playlist1 = Node(1, Node(2, Node(3, Node(4))))

playlist2 = Node(
    ("Respect", "Aretha Franklin"),
    Node(
        ("Superstition", "Stevie Wonder"),
        Node(
            ("Wonderwall", "Oasis"),
            Node(("Like a Prayer", "Madonna"), Node(("Bohemian Rhapsody", "Queen"))),
        ),
    ),
)

print_linked_list(shuffle_playlist(playlist1))
print_linked_list(shuffle_playlist(playlist2))
