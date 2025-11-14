def min_edges_to_connect(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    components = 0

    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    for node in range(n):
        if not visited[node]:
            dfs(node)
            components += 1

    min_edges = components - 1
    return min_edges


adj_matrix = [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0]]
print(min_edges_to_connect(adj_matrix))  # Output: 1
