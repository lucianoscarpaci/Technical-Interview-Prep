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


def remove_nth_from_end(head, n):
    temp = Node(0, head)
    first = temp
    second = temp

    for _ in range(n + 1):
        if first is None:
            return head
        first = first.next

    while first:
        first = first.next
        second = second.next

    if second.next:
        second.next = second.next.next

    return temp.next


head1 = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")

print_linked_list(remove_nth_from_end(head1, 2))
print_linked_list(remove_nth_from_end(head2, 1))
print_linked_list(remove_nth_from_end(head3, 1))
