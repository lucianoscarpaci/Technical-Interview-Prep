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


def playlist_overlap(playlist_a, playlist_b):
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    len_a = get_length(playlist_a)
    len_b = get_length(playlist_b)
    while len_a > len_b:
        playlist_a = playlist_a.next
        len_a -= 1
    while len_b > len_a:
        playlist_b = playlist_b.next
        len_b -= 1
    while playlist_a and playlist_b:
        if playlist_a == playlist_b:
            return playlist_a
        playlist_a = playlist_a.next
        playlist_b = playlist_b.next
    return None


playlist_a = Node("Song A", Node("Song B"))
playlist_b = Node("Song X", Node("Song Y", Node("Song Z")))
shared_segment = Node("Song M", Node("Song N", Node("Song O")))

playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment

print((playlist_overlap(playlist_a, playlist_b)).value)
