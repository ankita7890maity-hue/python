# Guess the output of the following code:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        if i == j:
            row_sum += matrix[i][j] * 2
        elif i + j == len(matrix) - 1:
            row_sum += matrix[i][j] * 3
        else:
            row_sum += matrix[i][j]
    result.append(row_sum)
print(result)