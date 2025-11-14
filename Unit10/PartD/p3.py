from collections import deque


def bfs(matrix, start):
    n = len(matrix)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in range(n):
            if matrix[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return result


adj_matrix = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]
print(bfs(adj_matrix, 0))
