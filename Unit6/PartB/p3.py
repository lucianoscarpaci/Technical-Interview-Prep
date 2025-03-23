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


def partition(suspect_ratings, threshold):
    # Partition the linked list such that all nodes with values greater
    # than threshold come before nodes with values less than or equal to
    # threshold.
    if not suspect_ratings:
        return None
    greater_head = Node(0)
    less_or_equal_head = Node(0)
    greater = greater_head
    less_or_equal = less_or_equal_head

    current = suspect_ratings
    while current:
        if current.value > threshold:
            greater.next = current
            greater = greater.next
        else:
            less_or_equal.next = current
            less_or_equal = less_or_equal.next
        current = current.next

    # combine the two lists
    greater.next = less_or_equal_head.next
    less_or_equal.next = None
    # check if greater list is empty or not
    if greater_head.next:
        return greater_head.next
    else:
        return less_or_equal_head.next


suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))

print_linked_list(partition(suspect_ratings, 3))
