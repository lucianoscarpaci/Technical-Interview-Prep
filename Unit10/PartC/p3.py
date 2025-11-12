from collections import deque


def get_all_destinations(flights, start):
    visited = set()
    queue = deque([start])
    while queue:
        destination = queue.popleft()
        for location in flights[destination]:
            if location not in visited:
                visited.add(location)  # Fix: Add location instead of destination
                queue.append(location)
    return visited


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": [],
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
