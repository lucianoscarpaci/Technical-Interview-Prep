def pascals(num_rows):
    store = {}
    def pascal(row, col):
        if row == 0 or col == 0 or row == col:
            return 1
        if (row, col) in store:
            return store[(row, col)]
        store[(row, col)] = pascal(row - 1, col - 1) + pascal(row - 1, col)
        return store[(row, col)]
    result = []
    for i in range(num_rows):
        result.append([pascal(i, j) for j in range(i + 1)])
    result.pop() # Remove the last row if it is [1]
    return result

numRows = 5
print(pascals(numRows))
numRows = 1
print(pascals(numRows))