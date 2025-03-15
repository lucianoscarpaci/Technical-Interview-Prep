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
        
def reverse_first_k(head, k):
	#given head reverse the k elements
    dummy = head
    move dummy k tim
    # return head of the reversed linked list
    # if k is larger than the length of the linked list, reverse the whole linked list

head = Node("apple", Node("cherry", Node("orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))
'''
orange -> cherry -> apple -> peach -> pear
'''
