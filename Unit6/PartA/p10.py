class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# Function to convert binary linked list to decimal
def locate_cache(cache_labels):
    result = 0
    current = cache_labels

    while current:
        result = result * 2 + current.value
        current = current.next
    return result

cache_labels = Node(1, Node(0, Node(1)))
print(locate_cache(cache_labels))  # 5