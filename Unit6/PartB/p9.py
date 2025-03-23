class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_duplicate_markers(trailhead):
    temp_head = Node(0)
    temp_head.next = trailhead
    prev = temp_head
    current = trailhead

    while current:
        # Check if current node has a duplicate
        if current.next and current.value == current.next.value:
            # Skip all the duplicates
            while current.next and current.value == current.next.value:
                current = current.next
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next
    return temp_head.next

trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))
print_linked_list(remove_duplicate_markers(trailhead))  # 1 -> 2 -> 4