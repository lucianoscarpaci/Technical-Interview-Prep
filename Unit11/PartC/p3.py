from collections import deque


def next_moves(position, grid):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_moves = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == 1:
                valid_moves.append((new_row, new_col))
    return valid_moves


def time_to_infect(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    safe_zones = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                safe_zones += 1

    if safe_zones == 0:
        return 0

    hours = 0

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for new_row, new_col in next_moves((row, col), grid):
                grid[new_row][new_col] = 2
                queue.append((new_row, new_col))
                safe_zones -= 1
        hours += 1


    return hours - 1 if safe_zones == 0 else -1


grid_1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

grid_2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

grid_3 = [[0, 2]]

print(time_to_infect(grid_1))
print(time_to_infect(grid_2))
print(time_to_infect(grid_3))
