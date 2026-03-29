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


# Determine which list contains more prime numbers
# The function returns the head of the list that has
# the greatest count of prime numbers.
def count_nodes_with_value(head, val):
    count = 0
    current = head
    while current:
        if current.value == val:
            count += 1
        current = current.next
    return count
