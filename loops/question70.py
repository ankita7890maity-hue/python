grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i + j) % 2 == 0:
            if grid[i][j] % 2 == 1:
                result.append(grid[i][j] ** 2)
            else:
                continue
        else:
            if grid[i][j] > 5:
                result.append(grid[i][j])
print(result)