from collections import deque


def next_moves(position, grid, visited):
    row, col = position
    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    valid_moves = []

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if (
            0 <= new_row < rows
            and 0 <= new_col < cols
            and not visited[new_row][new_col]
        ):
            valid_moves.append((new_row, new_col))

    return valid_moves


def nearest_zombie(grid):
    m, n = len(grid), len(grid[0])

    distances = [[-1 for _ in range(n)] for _ in range(m)]

    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(m)]
    # Start BFS from all zombies
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0:
                queue.append((row, col))
                visited[row][col] = True
                distances[row][col] = 0
    
    while queue:
        current = queue.popleft()
        for move in next_moves(current, grid, visited):
            visited[move[0]][move[1]] = True
            distances[move[0]][move[1]] = distances[current[0]][current[1]] + 1
            queue.append(move)
    return distances


grid_1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

grid_2 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

print(nearest_zombie(grid_1))
print(nearest_zombie(grid_2))
