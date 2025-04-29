def next_moves(position, visited, n):
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    valid_moves = []

    #explore all 4 directions in 3x3 grid
    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < n * 3 and 0 <= new_col < n * 3 and not visited[new_row][new_col]:
            valid_moves.append((new_row, new_col))
    return valid_moves

def dfs(position, visited, n):
    stack = [position]
    while stack:
        row, col = stack.pop()
        if not visited[row][col]:
            visited[row][col] = True
            # Get all valid moves from the current position
            stack.extend(next_moves((row, col), visited, n))

def count_regions(grid):
    n = len(grid)
    visited = [[False] * (n * 3) for _ in range(n * 3)]

    # Convert the grid into a 3x3 grid
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "/":
                visited[i * 3][j * 3 + 2] = True
                visited[i * 3 + 1][j * 3 + 1] = True
                visited[i * 3 + 2][j * 3] = True
            elif grid[i][j] == "\\":
                visited[i * 3][j * 3] = True
                visited[i * 3 + 1][j * 3 + 1] = True
                visited[i * 3 + 2][j * 3 + 2] = True
        # count regions using dfs
        regions = 0
        for r in range(n * 3):
            for c in range(n * 3):
                if not visited[r][c]:
                    dfs((r, c), visited, n)
                    regions += 1
        return regions

grid_1 = [" /","/ "]

print(count_regions(grid_1))

grid_3 = ["/\","" \/"]

print(count_regions(grid_3))