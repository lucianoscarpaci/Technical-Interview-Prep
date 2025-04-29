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


def flood_fill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image

    original_color = image[sr][sc]
    m, n = len(image), len(image[0])
    visited = [[False] * n for _ in range(m)]

    dfs(sr, sc, image, visited, original_color)

    for r in range(m):
        for c in range(n):
            if visited[r][c]:
                image[r][c] = color

    return image


# Example usage
image = [[0, 0, 0], [0, 0, 0]]
sr, sc = 0, 0
color = 0
print(flood_fill(image, sr, sc, color))  # Output: [[0, 0, 0], [0, 0, 0]]
