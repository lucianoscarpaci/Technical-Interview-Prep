def dfs(matrix, start):
    visited = set()
    result = []

    def dfs_recursive(node):
        visited.add(node)
        result.append(node)
        for neighbor in range(len(matrix[node])):
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                dfs_recursive(neighbor)
    dfs_recursive(start)
    return result

matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
start = 0
print(dfs(matrix, start))