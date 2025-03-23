class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def trail_length(trail):
    length = 0
    tail = trail
    while tail.next:
        length += 1
        tail = tail.next
        if tail == trail:
            break
    return length

marker1 = Node("Marker 1")
marker2 = Node("Marker 2")
marker3 = Node("Marker 3")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker1
print(trail_length(marker1))  # 3