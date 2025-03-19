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


def increment_ll(head):
    node = head
    carry = 1
    while node:
        node.value += carry
        node.next.value += carry
        node.next.next.value += carry
        if node.value < 10:
            return head
    return head


node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(increment_ll(node_one))
# Output List: 6 -> 7 -> 8
