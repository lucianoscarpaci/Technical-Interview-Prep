class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def most_primes_list(head_a, head_b):
    if head_a is None and head_b is None:
        return None

    # Initialize prime counts
    primes_a_count = 0
    primes_b_count = 0

    # Traverse the first linked list and count primes
    current_a = head_a
    while current_a:
        if is_prime(current_a.data):
            primes_a_count += 1
        current_a = current_a.next

    # Traverse the second linked list and count primes
    current_b = head_b
    while current_b:
        if is_prime(current_b.data):
            primes_b_count += 1
        current_b = current_b.next

    # Compare the counts and return the appropriate head
    if primes_a_count > primes_b_count:
        return head_a
    elif primes_b_count > primes_a_count:
        return head_b
    else:
        # In case of a tie, return the head with the smaller data value
        return head_a if head_a.data < head_b.data else head_b


# Example usage
# Create linked lists and test the function
list1 = SinglyLinkedList()
list1.insert_node(2)
list1.insert_node(4)
list1.insert_node(6)

list2 = SinglyLinkedList()
list2.insert_node(3)
list2.insert_node(5)
list2.insert_node(7)

# Call the function
result_head = most_primes_list(list1.head, list2.head)
print(f"List with more primes starts with: {result_head.data}")
