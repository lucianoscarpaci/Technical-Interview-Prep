def has_cycle(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n

    def dfs(current, parent):
        visited[current] = True
        for neighbor in range(n):
            if adj_matrix[current][neighbor] == 1:
                if not visited[neighbor]:
                    if dfs(neighbor, current):
                        return True
                elif neighbor != parent:
                    return True
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

print(has_cycle(adj_matrix))