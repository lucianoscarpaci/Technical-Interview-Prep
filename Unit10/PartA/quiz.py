def bfs(matrix, start):
    visited = set()
    result = []

    def bfs_recursive(node):

        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in matrix[node]:
                bfs_recursive(neighbor)

    bfs_recursive(start)
    return result


graph = {"A": ["B", "D"], "B": ["C"], "D": ["E"], "E": ["F"]}

print(graph.keys())
