class Node:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next


def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def count_critical_points(song_audio):
    # The third is a local minima because 1 is less than 3&2
    # The fifth is a local maxima because 5 is greater than 1&2
    # The sixth is a local minima because 1 is less than 5&2
    current = song_audio
    critical_points = 0
    while current.next:
        if current.song < current.next.song:
            critical_points += 1
        current = current.next

    return critical_points


song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))
