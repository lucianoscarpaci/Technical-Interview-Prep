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


def add_two_numbers(head_a, head_b):
    temp_head = Node(0)
    current = temp_head
    carry = 0
    while head_a or head_b or carry:
        sum_value = carry
        if head_a:
            sum_value += head_a.value
            head_a = head_a.next
        if head_b:
            sum_value += head_b.value
            head_b = head_b.next
        carry = sum_value // 10
        current.next = Node(sum_value % 10)
        current = current.next
    return temp_head.next


head_a = Node(2, Node(4, Node(3)))
head_b = Node(5, Node(6, Node(4)))
print_linked_list(add_two_numbers(head_a, head_b))  # 7 -> 0 -> 8
