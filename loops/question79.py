# Guess the output of the following code:
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        neighbors = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[ni]):
                    neighbors.append(matrix[ni][nj])
        if len(neighbors) >= 3:
            result.append(sum(neighbors) // len(neighbors))
print(result)