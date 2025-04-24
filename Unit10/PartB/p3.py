from collections import deque


def counting_flights(flights, start, destination):
    n = len(flights)
    if start == destination:
        return 0

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current_airport, num_flights = queue.popleft()
        for next_airport in range(n):
            if (
                flights[current_airport][next_airport] == 1
                and next_airport not in visited
            ):
                if next_airport == destination:
                    return num_flights + 1
                queue.append((next_airport, num_flights + 1))
                visited.add(next_airport)
    return -1


# Example usage
flights = [
    [0, 1, 1, 0, 0],  # Airport 0
    [0, 0, 1, 0, 0],  # Airport 1
    [0, 0, 0, 1, 0],  # Airport 2
    [0, 0, 0, 0, 1],  # Airport 3
    [0, 0, 0, 0, 0],  # Airport 4
]

print(counting_flights(flights, 0, 2))
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
