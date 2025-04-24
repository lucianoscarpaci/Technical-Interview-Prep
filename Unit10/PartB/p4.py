def num_airline_regions(is_connected):
    n = len(is_connected)
    visited = set()
    num_regions = 0
    def dfs(i):
        visited.add(i)
        for j in range(n):
            if is_connected[i][j] == 1 and j not in visited:
                dfs(j)
    for i in range(n):
        if i not in visited:
            dfs(i)
            num_regions += 1
    return num_regions


is_connected1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

is_connected2 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]

print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2))
