# Helper function to find valid next moves
def next_moves(position, grid, visited):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])

    # Define directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # List to hold the valid next moves
    valid_moves = []

    # Check each direction
    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        # Ensure new position is within the grid bounds, is a safe zone, and not visited
        if (
            0 <= new_row < rows
            and 0 <= new_col < cols
            and grid[new_row][new_col] == 1
            and (new_row, new_col) not in visited
        ):
            valid_moves.append((new_row, new_col))
    return valid_moves


def explore_safe_zone(row, col, grid, visited):
    visited.add((row, col))
    size = 1

    for next_row, next_col in next_moves((row, col), grid, visited):
        size += explore_safe_zone(next_row, next_col, grid, visited)
    return size


def largest_safe_zone(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    largest_area = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                area = explore_safe_zone(row, col, grid, visited)
                largest_area = max(largest_area, area)
    return largest_area


grid = [
    [0, 0, 0, 1, 1],  # Row 0
    [0, 0, 0, 1, 1],  # Row 1
    [1, 1, 1, 0, 0],  # Row 2
    [1, 1, 1, 1, 0],  # Row 3
    [0, 0, 0, 1, 0],  # Row 4
]

print(largest_safe_zone(grid))
"""
10 IS THE LARGEST SAFE ZONE
"""
