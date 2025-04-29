from collections import deque


def has_path(city):
    m, n = len(city), len(city[0])

    # If the entrance or the safehouse is blocked, there's no path
    if city[0][0] == 0 or city[m - 1][n - 1] == 0:
        return False

    # BFS to check if there's a path from (0, 0) to (m-1, n-1)
    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True

    while queue:
        row, col = queue.popleft()

        # If we reached the bottom-right corner, return True
        if row == m - 1 and col == n - 1:
            return True

        # Explore the right and downward directions
        for new_row, new_col in [(row + 1, col), (row, col + 1)]:
            if (
                0 <= new_row < m
                and 0 <= new_col < n
                and not visited[new_row][new_col]
                and city[new_row][new_col] == 1
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col))

    return False


def can_disconnect_safehouse(city):
    m, n = len(city), len(city[0])

    if not has_path(city):
        return True

    for row in range(m):
        for col in range(n):
            if (row == 0 and col == 0) or (row == m - 1 and col == n - 1):
                continue

            city[row][col] = 1 - city[row][col]

            if not has_path(city):
                return True

            city[row][col] = 1 - city[row][col]
    return False


city_1 = [[1, 1, 1], [0, 0, 1], [1, 1, 1]]

city_2 = [[1, 0, 0], [1, 1, 0], [0, 1, 1]]

print(can_disconnect_safehouse(city_1))
print(can_disconnect_safehouse(city_2))
