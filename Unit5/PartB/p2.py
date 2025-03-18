# Connect the node instances to create the linked list: K.K. Slider -> Harriet -> Saharah -> Isabelle


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


kk_slider = Node("K.K. Slider", "Harriet")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
# Link nodes together
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
# Print linked list
print_linked_list(kk_slider)
