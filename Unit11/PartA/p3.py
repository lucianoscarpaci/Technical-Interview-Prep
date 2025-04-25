def next_moves(position, grid, visited):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])

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
    target = (rows - 1, cols - 1)

    def dfs(row, col, visited):
        if (row, col) == target:
            return True

        visited.add((row, col))

        for next_move in next_moves((row, col), grid, visited):
            if dfs(next_move[0], next_move[1], visited):
                return True
        return False
        # start dfs from the start position

    visited = set()
    return dfs(position[0], position[1], visited)


def list_all_escape_routes(grid):
    rows, cols = len(grid), len(grid[0])
    escape_routes = []

    # check each cell in the grid
    for row in range(rows):
        for col in range(cols):
            if (
                grid[row][col] == 1
                and can_move_safely((row, col), grid)
            ):
                escape_routes.append((row, col))

    return escape_routes


grid = [
    [1, 0, 1, 0, 1],  # Row 0
    [1, 1, 1, 1, 0],  # Row 1
    [0, 0, 1, 0, 0],  # Row 2
    [1, 0, 1, 1, 1],  # Row 3
]

print(list_all_escape_routes(grid))
