def next_moves(position, grid, visited):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    moves = []
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                moves.append((new_row, new_col))
    return moves


def can_move_safely(position, grid):
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
        for next_move in next_moves((row, col), grid, visited):
            if dfs(next_move[0], next_move[1]):
                return True

        return False

    return dfs(start_row, start_col)


grid = [
    [1, 0, 1, 1, 0],  # Row 0
    [1, 1, 1, 1, 0],  # Row 1
    [0, 0, 1, 1, 0],  # Row 2
    [1, 0, 1, 1, 1],  # Row 3
]

position_1 = (0, 0)
position_2 = (0, 4)
position_3 = (3, 0)

print(can_move_safely(position_1, grid))
print(can_move_safely(position_2, grid))
print(can_move_safely(position_3, grid))



def list_all_escape_routes(grid):
    rows, cols = len(grid), len(grid[0])
    target = (rows - 1, cols - 1)
    all_routes = []

    def dfs(position, path, visited):
        if position == target:
            all_routes.append(path.copy())
            return
        visited.add(position)
        for next_move in next_moves(position, grid, visited):
            path.append(next_move)
            dfs(next_move, path, visited)
            path.pop()
        visited.remove(position)

    if grid[0][0] == 1:
        dfs((0, 0), [(0, 0)], set())
    return all_routes

