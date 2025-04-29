from collections import deque


def bfs_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()

        # Check if the destination is reached
        if node == destination:
            return path

        # Mark the current node as visited
        if node not in visited:
            visited.add(node)
            # Enqueue neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    # If no path is found
    return None
