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


def add_second(head, val):
    if head is None:
        return Node(val)
    second = Node(val, head.next)
    head.next = second
    return head


original_list_head = Node("banana")
second = Node("blue shell")
third = Node("bullet bill")
original_list_head.next = second
second.next = third
# Linked list: "banana" -> "blue shell" -> "bullet bill"
new_list = add_second(original_list_head, "red shell")
print_linked_list(new_list)
