class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_circular(clues):
    if not clues:
        return None
    
    slow = fast = clues
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))
