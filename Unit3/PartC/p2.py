from collections import deque


def reveal_attendee_list_in_order(attendees):
    n = len(attendees)
    index_queue = deque(range(n))
    result = [0] * n

    for attendee in sorted(attendees):
       result[index_queue.popleft()] = attendee
       if index_queue:
        index_queue.append(index_queue.popleft())
    return result
     


print(reveal_attendee_list_in_order([17, 13, 11, 2, 3, 5, 7]))
print(reveal_attendee_list_in_order([1, 1000]))
