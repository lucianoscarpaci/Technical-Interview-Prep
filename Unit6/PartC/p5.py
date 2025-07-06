class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


def double_listeners(monthly_listeners):
    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    head = reverse_list(monthly_listeners)
    current = head
    carry = 0
    while current:
        doubled_value = current.value * 2 + carry
        current.value = doubled_value % 10
        carry = doubled_value // 10
        if current.next is None and carry > 0:
            current.next = Node(carry)
            break
        current = current.next
    return reverse_list(head)


monthly_listeners1 = Node(1, Node(8, Node(9)))  # 189
monthly_listeners2 = Node(9, Node(9, Node(9)))  # 999

print_linked_list(double_listeners(monthly_listeners1))
print_linked_list(double_listeners(monthly_listeners2))
