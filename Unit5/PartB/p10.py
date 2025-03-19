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


def copy_ll(head):
    current = head
    while current:
        current = current.next
    return head


mario = Node("Mario")
daisy = Node("Daisy")
luigi = Node("Luigi")
mario.next = daisy
daisy.next = luigi
head = mario
# Linked List: Mario -> Daisy -> Luigi
copy = copy_ll(mario)

# Change original list -- should not affect the copy
mario.value = "Original Mario"
print_linked_list(head)  # Original Mario -> Daisy -> Luigi
mario.value = "Mario"
print_linked_list(copy)  # Mario -> Daisy -> Luigi
