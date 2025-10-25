def delete_node(head, val):
    temp_head = Node("temp")  # Initialize a temporary head node
    temp_head.next = head  # Point the temporary head at the input list

    # Traverse the list
    previous = temp_head
    current = head
    while current:
        if current.value == val:  # If the current node is the node to delete
            previous.next = current.next  # Delete the node
            break  # Break out of the loop

        previous = current
        current = current.next
    return temp_head.next  # Return the head of the input list
