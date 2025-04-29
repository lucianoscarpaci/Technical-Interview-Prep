def next_moves(position, safety, visited):
    row, col = position
    rows, cols = len(safety), len(safety[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    valid_moves = []

    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < rows and 0 <= new_col < cols:
            # Check if the next zone is less or equally safe
            if (
                safety[new_row][new_col] >= safety[row][col]
                and (new_row, new_col) not in visited
            ):
                valid_moves.append((new_row, new_col))

    return valid_moves


def dfs(row, col, safety, visited):
    stack = [(row, col)]
    visited.add((row, col))

    while stack:
        current_row, current_col = stack.pop()
        for next_row, next_col in next_moves(
            (current_row, current_col), safety, visited
        ):
            if (next_row, next_col) not in visited:
                visited.add((next_row, next_col))
                stack.append((next_row, next_col))


def escape_subzones(safety):
    m, n = len(safety), len(safety[0])

    # sets to track visited zones
    left_reachable = set()
    right_reachable = set()

    for r in range(m):
        dfs(r, 0, safety, left_reachable)
        dfs(r, n - 1, safety, right_reachable)

    for c in range(n):
        dfs(0, c, safety, left_reachable)
        dfs(m - 1, c, safety, right_reachable)

    # check zones that can reach both sides
    result = []
    for r in range(m):
        for c in range(n):
            if (r, c) in left_reachable and (r, c) in right_reachable:
                result.append((r, c))
    return result


safety_1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]

safety_2 = [[2, 1], [1, 2]]

print(escape_subzones(safety_1))
print(escape_subzones(safety_2))
