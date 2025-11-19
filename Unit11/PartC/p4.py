def next_moves(position, visited, n):
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_moves = []

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < n * 3 and 0 <= new_col < n * 3 and not visited[new_row][new_col]:
            valid_moves.append((new_row, new_col))
        return valid_moves

def dfs(position, visited, n):
    stack = [position]
    while stack:
        current = stack.pop()

def count_regions(grid):
    pass

grid_1 = [" /","/ "]

print(count_regions(grid_1))

grid_2 = [" /","  "]

print(count_regions(grid_2))

grid_3 = ["/\","\/"]

print(count_regions(grid_3))