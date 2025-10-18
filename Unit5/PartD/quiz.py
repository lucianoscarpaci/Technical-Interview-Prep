"""
Desc
Given the head of a singly linked list, return the middle node of the linked list
Example:
head = [1,2,3,4,5]
output = [3,4,5]
UNDERSTAND:
Trying to find the middle by making current pointer to the middle.
When it returns should be the middle.
Return the middle node not the value.
INPUT: List of nodes.
OUTPUT: The middle node of linked list
CONDITIONS: Moving the pointer to the middle.
EDGE CASES: While the current is empty and current next node is empty
then return empty list.
If we have more than two nodes
MATCH and PLAN:
- Singly linked list
- slow fast pointer method
- head = None
- set slow = fast = head
- while current and current next
- update the current pointer to the middle
- return the current pointer
"""


def middle_node(head):
    if not head:
        return []

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
