def next_moves(position, grid, visited):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_moves = []

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if (
            0 <= new_row < rows
            and 0 <= new_col < cols
            and grid[new_row][new_col] == 1
            and (new_row, new_col) not in visited
        ):
            valid_moves.append((new_row, new_col))
    return valid_moves


def can_move_safely(position, grid):
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = position
    target = (rows - 1, cols - 1)

    if grid[start_row][start_col] == 0 or grid[rows - 1][cols - 1] == 0:
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
