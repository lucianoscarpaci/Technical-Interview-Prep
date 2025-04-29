# Input: grid1 = [[1,0,1,0,1]],[1,1,1,1,1],[0,0,0,0,0],
# [1,1,1,1,1],[1,0,1,0,1]], 
# grid2 = [0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
#Output: 2


def next_moves(position, grid, visited, original_color):
    row, col = position
    rows, cols = len(grid), len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    valid_moves = []

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if (0 <= new_row < rows and
                0 <= new_col < cols and
                not visited[new_row][new_col] and
                grid[new_row][new_col] == original_color):
            valid_moves.append((new_row, new_col))

    return valid_moves



def dfs(row, col, grid, visited, original_color):
    stack = [(row, col)]
    visited[row][col] = True

    while stack:
        current_row, current_col = stack.pop()
        for next_row, next_col in next_moves(
            (current_row, current_col), grid, visited, original_color
        ):
            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                stack.append((next_row, next_col))


def count_sub_islands(grid1, grid2):
    if not grid1 or not grid2:
        return 0

    m, n = len(grid1), len(grid1[0])
    visited = [[False] * n for _ in range(m)]
    count = 0

    for row in range(m):
        for col in range(n):
            if (grid1[row][col] == 1 and
                    grid2[row][col] == 1 and
                    not visited[row][col]):
                dfs(row, col, grid2, visited, grid2[row][col])
                count += 1

    return count

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],
[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(count_sub_islands(grid1, grid2))  # Output: 2