class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mystery_function(head):
    if not head:
        return None

    total = 0
    current = head

    while current:
        total += current.val
        current.val = total
        current = current.next
    return head


def print_singly_linked_list(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
output = mystery_function(head)
print_singly_linked_list(output)  # Expected output: 1 -> 3 -> 6 -> 10
