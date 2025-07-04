class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next


def catch_fish(head):
    if head is None:
        return None
    else:
        print(f"Catch: {head.fish_name}")
        return head.next


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))
