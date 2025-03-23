class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def merge_timelines(known_timeline, witness_timeline):
    temp_head = Node(0)  # temporary head for the merged list
    current = temp_head  # pointer to build the new list
    # Pointers to traverse the two lists
    p1 = known_timeline
    p2 = witness_timeline

    while p1 and p2:
        if p1.value <= p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    # If any of the lists has elements left
    if p1:
        current.next = p1
    else:
        current.next = p2
    return temp_head.next


known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))
print_linked_list(merge_timelines(known_timeline, witness_timeline))
