from collections import deque


def bfs_path(graph, start, destination):
    # Initialize the queue with a tuple containing the start node and the initial path
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        # Unpack the current node and path from the queue
        node, path = queue.popleft()

        # If the destination is found, return the current path
        if node == destination:
            return path

        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                # Append the neighbor and updated path to the queue
                queue.append((neighbor, path + [neighbor]))

    # Return None if no path is found
    return None


# Example usage:
graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
start_node = 0
destination_node = 4
print(
    bfs_path(graph, start_node, destination_node)
)  # Output: [0, 1, 3, 4] or [0, 2, 3, 4]
