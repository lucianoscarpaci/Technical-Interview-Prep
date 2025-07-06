class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def count_nodes(head, val):
    count = 0
    current = head
    while current.next:
        if current == None:
            break
        if current.value == val:
            count += 1
        current = current.next
    if current.value == val:
        count += 1
    return count