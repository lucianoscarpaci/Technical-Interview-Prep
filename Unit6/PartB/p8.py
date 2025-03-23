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


def clear_trail(trailhead):
    if not trailhead:
        return None
    
    slow = fast = trailhead
    # Find the cycle using Floyd's cycle-finding algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle found
        return trailhead
    # Find the start of the cycle
    slow = trailhead
    while slow != fast:
        slow = slow.next
        fast = fast.next
    # Remove the cycle
    while fast.next != slow:
        fast = fast.next
    fast.next = None
    return trailhead

marker1 = Node("Trailhead")
marker2 = Node("Trail Fork")
marker3 = Node("The Falls")
marker4 = Node("Peak")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker4
marker4.next = marker1
print_linked_list(clear_trail(marker1))