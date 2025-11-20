import heapq

def maxProbability(n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
    """
    Finds the path with the maximum probability of success to go from start to end.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges, where each edge is a list of two nodes.
        succProb: A list of success probabilities for each edge.
        start_node: The starting node.
        end_node: The ending node.

    Returns:
        The maximum probability of success to go from start to end.
    """

    graph = [[] for _ in range(n)]
    for i, edge in enumerate(edges):
        u, v = edge
        probability = succProb[i]
        graph[u].append((v, probability))
        graph[v].append((u, probability))

    probabilities = [0.0] * n
    probabilities[start_node] = 1.0

    pq = [(-1.0, start_node)]  # Use a max-heap (negate probabilities)

    while pq:
        prob, node = heapq.heappop(pq)
        prob = -prob  # Revert the negation

        if prob < probabilities[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = prob * edge_prob
            if new_prob > probabilities[neighbor]:
                probabilities[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return round(probabilities[end_node], 5)

print(maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))  # Output: 0.25
