def find_center(terminals):
    count = {}

    for u, v in terminals:
        count[u] = count.get(u, 0) + 1
        count[v] = count.get(v, 0) + 1
    
    for terminal, c in count.items():
        if c > 1:
            return terminal

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))
