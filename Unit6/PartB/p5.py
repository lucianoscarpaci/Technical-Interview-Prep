class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head
    # Step 1: Calculate the length of the new list
    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next
    # Step 2: Normalize k
    k = k % length
    if k == 0:
        return head
    # Step 3: Find the new head
    new_tail_position = length - k - 1
    new_tail = head
    for _ in range(new_tail_position):
        new_tail = new_tail.next
    new_head = new_tail.next
    # Step 4: Rotate the list
    tail.next = head
    new_tail.next = None
    # Step 5: Return the new head
    return new_head


evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))