class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next


# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()


node_one = SongNode("Uptown Funk")
node_two = SongNode("Party Rock Anthem")
node_three = SongNode("Bad Romance")
node_one.next = node_two
node_two.next = node_three
top_hits_2010s = SongNode(node_one.song, node_one.next)
print_linked_list(top_hits_2010s)
