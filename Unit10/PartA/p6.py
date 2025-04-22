from collections import deque


def get_all_destinations(flights, start):
    queue = deque([start])
    visited = set([start])

    reachable = []

    while queue:
        current = queue.popleft()
        reachable.append(current)

        for destination in flights.get(current, []):
            if destination not in visited:
                visited.add(destination)
                queue.append(destination)
    return reachable


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo"],
}

print(get_all_destinations(flights, "Tokyo"))
