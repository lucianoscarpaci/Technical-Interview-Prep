import heapq


def kthSmallest(matrix, k):
    n = len(matrix)
    min_heap = []

    # Initialize the heap with the first element of each row
    for r in range(min(k, n)):  # Only need to consider up to k rows
        heapq.heappush(min_heap, (matrix[r][0], r, 0))

    # Extract the smallest element from the heap k times
    for _ in range(k):
        element, r, c = heapq.heappop(min_heap)
        if c + 1 < n:  # If there is a next element in the same row
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

    return element


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
print(kthSmallest(matrix, k))  # Output: 13
matrix = [[-5]]
k = 1
print(kthSmallest(matrix, k))  # Output: -5
matrix = [[1, 2], [1, 3]]
k = 2
print(kthSmallest(matrix, k))  # Output: 1
matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
k = 5
print(kthSmallest(matrix, k))  # Output: 6
