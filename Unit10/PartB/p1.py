from collections import deque

def can_rebook(flights, source, dest):
    if source == dest:
        return True
    visited = []
    queue = deque([source])
    while queue:
        current = queue.popleft()
        visited.append(current)

        for i in range(len(flights[current])):
            if flights[current][i] == 1 and i not in visited:
                if i == dest:
                    return True
                queue.append(i)
    return False


flights1 = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]  # Flight 0  # Flight 1  # Flight 2

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2))
