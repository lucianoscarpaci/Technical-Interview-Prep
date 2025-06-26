def get_sum_of_odds(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    count_of_odds = 0
    sum_of_odds = 0
    # Iterate through each element
    for i in range(rows):
        for j in range(cols):
            # Check if the element is odd
            if matrix[i][j] % 2 != 0:
                # count the odd numbers in the matrix
                count_of_odds += 1
                sum_of_odds += matrix[i][j]
    return [count_of_odds, sum_of_odds]


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(get_sum_of_odds(matrix))  # Output should be [6, 36]
