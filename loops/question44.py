# Guess the output of the following code:
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for num in row:
        if num == 4:
            break
        print(num)
