class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next


# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    artist = {}
    current = playlist
    while current:
        if current.artist in artist:
            artist[current.artist] += 1
        else:
            artist[current.artist] = 1
        current = current.next
    return artist


playlist = SongNode(
    "Saturn",
    "SZA",
    SongNode(
        "Who",
        "Jimin",
        SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA")),
    ),
)

print(
    get_artist_frequency(playlist)
)  # Expected output: {'SZA': 2, 'Jimin': 1, 'Sabrina Carpenter': 1}
