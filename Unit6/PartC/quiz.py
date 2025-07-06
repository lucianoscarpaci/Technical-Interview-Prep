class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()


def delete_node(head, key):
    if head is None:
        return None

    if head.data == key:
        return head.next

    prev = None
    current = head

    while current:
        if current.data == key:
            prev.next = current.next
            return head
        prev = current
        current = current.next
    return head


head = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
print_linked_list(head)
