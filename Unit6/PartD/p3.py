#Given the tail of a 0-indexed doubly linked list
# and a value val, implement a function that returns
# the smallest index of a node with value val, in the list.
# If no node with value val exists, return -1.
def find_smallest_index(tail, val):
    index = 0
    current = tail

    # Traverse the list backwards
    while current:
        if current.val == val:  # If the current node has the target value
            return index  # Return the current index

        current = current.prev  # Move to the previous node
        index += 1  # Increment the index

    return -1  # If no node with value val exists, return -1