from collections import defaultdict


def find_smallest_set(n, edges):
    graph = defaultdict(list)
    visited = [False] * n
    smallest_set = set()

    # Define the DFS function that will mark nodes as visited
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    # Construct the adjacency list for the graph
    for u, v in edges:
        graph[u].append(v)

    # Traverse each node
    for i in range(n):
        # If the node hasn't been visited, it's a new starting point
        if not visited[i]:
            smallest_set.add(i)
            dfs(i)  # Perform DFS from this node
    return list(smallest_set)


n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
print(find_smallest_set(n, edges))
