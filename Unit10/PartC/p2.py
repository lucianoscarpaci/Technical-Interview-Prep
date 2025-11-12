def find_center(terminals):
    return [
        i for i, x in enumerate(terminals) if all(i in y for y in terminals if y != x)
    ][0]


terminals1 = [[1, 2], [2, 3], [4, 2]]
terminals2 = [[1, 2], [5, 1], [1, 3], [1, 4]]

print(find_center(terminals1))
print(find_center(terminals2))
