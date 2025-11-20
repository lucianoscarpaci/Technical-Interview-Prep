def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, suffix):
        if len(suffix) == 0:
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != suffix[0]:
            return False

        ret = False
        temp = board[r][c]
        board[r][c] = "#"
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for row_offset, col_offset in directions:
            ret = backtrack(r + row_offset, c + col_offset, suffix[1:])
            if ret:
                break

        board[r][c] = temp
        return ret

    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, word):
                return True

    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCCED"
print(exist(board, word1))  # Output: True
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word2 = "ABCB"
print(exist(board, word2))  # Output: False
