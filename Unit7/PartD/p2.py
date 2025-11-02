class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next


# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_linked_list(head)
print("Reversed linked list:")
print_linked_list(reversed_head)
