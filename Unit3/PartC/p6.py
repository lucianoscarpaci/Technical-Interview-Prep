from collections import deque


def mark_event_timeline(event, timeline):
    t_len = len(timeline)
    event_len = len(event)
    queue = deque([(["?"] * t_len, [])])
    max_turns = 10 * t_len

    def can_place(t, event, start):
        for i in range(event_len):
            if t[start + i] != "?" and t[start + i] != event[i]:
                return False
        return True

    def place_event(t, event, start):
        new_t = t[:]
        for i in range(event_len):
            new_t[start + i] = event[i]
        return new_t

    turns = 0
    while queue and turns < max_turns:
        current_t, indices = queue.popleft()
        for i in range(t_len - event_len + 1):
            if can_place(current_t, event, i):
                new_t = place_event(current_t, event, i)
                new_indices = indices + [i]
                if ''.join(new_t) == timeline:
                    return new_indices
                queue.append((new_t, new_indices))
        turns += 1 

    return []


print(mark_event_timeline("abc", "ababc"))
print(mark_event_timeline("abca", "aabcaca"))
