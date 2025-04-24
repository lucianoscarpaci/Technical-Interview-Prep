def can_rebook(flights, source, dest):
    n = len(flights)
    visited = [False] * n

    def dfs(current):
        if current == dest:
            return True
        visited[current] = True

        for neighbor in range(n):
            if flights[current][neighbor] == 1 and not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False
    return dfs(source)

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 