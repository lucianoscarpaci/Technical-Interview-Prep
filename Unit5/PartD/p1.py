# Given the head of a singly linked list, return
# a dictionary that maps ListNode values to their
# Frequency in the given list.
def linked_list_frequencies(head):
    frequencies = {}
    current = head
    while current:
        if current.val in frequencies:
            frequencies[current.val] += 1
        else:
            frequencies[current.val] = 1
        current = current.next
    return frequencies
