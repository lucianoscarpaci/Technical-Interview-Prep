def next_moves(position, grid):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    valid_moves = []

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
            valid_moves.append((new_row, new_col))
    return valid_moves


grid = [
    [0, 0, 0, 1, 1],  # Row 0
    [0, 0, 0, 1, 1],  # Row 1
    [1, 1, 1, 0, 0],  # Row 2
    [1, 1, 1, 1, 0],  # Row 3
    [0, 0, 0, 1, 0],  # Row 4
]

position_1 = (3, 2)
position_2 = (0, 4)
position_3 = (0, 1)

print(next_moves(position_1, grid))
print(next_moves(position_2, grid))
print(next_moves(position_3, grid))
"""
[(2, 2), (3, 1), (3, 3)]
[(1, 4), (0, 3)]
[]
"""
position_4 = (0, 0)
position_5 = (4, 0)
print(next_moves(position_4, grid))
print(next_moves(position_5, grid))
"""
[(2, 2), (3, 1), (3, 3)]
[(1, 4), (0, 3)]
[]
[]
[(3, 0)]
"""
