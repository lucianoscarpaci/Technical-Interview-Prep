def next_moves(position, grid, visited):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_moves = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                valid_moves.append((new_row, new_col))
    return valid_moves


def can_reach_safe_haven(position, grid):
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = position
    target = (rows - 1, cols - 1)

    if grid[start_row][start_col] == 0 or grid[target[0]][target[1]] == 0:
        return False

    visited = set()

    def dfs(row, col):
        if (row, col) == target:
            return True
        visited.add((row, col))
        for next_row, next_col in next_moves((row, col), grid, visited):
            if (next_row, next_col) not in visited:
                if dfs(next_row, next_col):
                    return True
        return False

    return dfs(start_row, start_col)


def list_all_escape_routes(grid):
    rows, cols = len(grid), len(grid[0])
    target = (rows - 1, cols - 1)
    all_routes = []

    def dfs(path, position, visited):
        if position == target:
            all_routes.append(path.copy())
            return
        visited.add(position)
        for next_pos in next_moves(position, grid, visited):
            if next_pos not in visited:
                path.append(next_pos)
                dfs(path, next_pos, visited)
                path.pop()
        visited.remove(position)

    start_position = (0, 0)
    if grid[0][0] == 1:
        dfs([start_position], start_position, set())
    return all_routes


grid = [
    [1, 0, 1, 0, 1],  # Row 0
    [1, 1, 1, 1, 0],  # Row 1
    [0, 0, 1, 0, 0],  # Row 2
    [1, 0, 1, 1, 1],  # Row 3
]

print(list_all_escape_routes(grid))
