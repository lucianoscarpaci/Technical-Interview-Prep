def next_moves(position, city):
    row, col = position
    rows, cols = len(city), len(city[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    valid_moves = []
    
    for d_row, d_col in directions:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < rows and 0 <= new_col < cols and city[new_row][new_col] < city[row][col]:
            valid_moves.append((new_row, new_col))
    
    return valid_moves


def dfs(row, col, city, memo):
    if memo[row][col] != -1:
        return memo[row][col]
    
    max_length = 1

    for new_row, new_col in next_moves((row, col), city):
        max_length = max(max_length, 1 + dfs(new_row, new_col, city, memo))
    
    memo[row][col] = max_length
    return max_length

def longest_decreasing_path(city):
    if not city or not city[0]:
        return 0
    
    m, n = len(city), len(city[0])
    memo = [[-1] * n for _ in range(m)]
    longest_path = 0

    for row in range(m):
        for col in range(n):
            longest_path = max(longest_path, dfs(row, col, city, memo))
    return longest_path

city_1 = [
    [4, 3],
    [1, 2]
]

city_2 = [
    [1, 2, 18, 3],
    [26, 6, 7, 15],
    [9, 10, 17, 18],
    [14, 15, 16, 22]
]

print(longest_decreasing_path(city_1))
print(longest_decreasing_path(city_2))
