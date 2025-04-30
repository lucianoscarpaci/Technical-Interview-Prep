def all_paths(graph):
    result = []

    def dfs(node, path):
        if node == len(graph) - 1:
            result.append(path[:])
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()
    dfs(0, [0])
    return result

graph_1 = [[1,2],[3],[3],[]]
print(all_paths(graph_1))
graph_2 = [[4,3,1],[3,2,4],[3],[4],[]]
print(all_paths(graph_2))
graph_3 = [[5, 2],[5],[4],[3],[5],[]]
print(all_paths(graph_3))