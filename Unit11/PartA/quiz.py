"""
Example 1:

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0]
]

print(max_area_of_island(grid))  # Output: 4


Example 2:

grid = [
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 1]
]

print(max_area_of_island(grid))  # Output: 5
"""


def next_moves(position, grid):
    row, col = position
    rows, cols = len(grid), len(grid[0])

    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # List to hold the valid next moves
    valid_moves = []

    # Check each direction
    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        # Ensure the new position is within the grid bounds and is a safe zone (1)
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
            valid_moves.append((new_row, new_col))

    return valid_moves


def max_area_of_island(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_area = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return 0
        if grid[row][col] == 0 or visited[row][col]:
            return 0

        visited[row][col] = True
        area = 1

        for next_row, next_col in next_moves((row, col), grid):
            area += dfs(next_row, next_col)

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                max_area = max(max_area, dfs(r, c))

    return max_area

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0]
]

print(max_area_of_island(grid))  # Output: 4
