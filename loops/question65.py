matrix = [[1, 2], [3, 4], [5, 6]]
result = []
for row in matrix:
    for i, val in enumerate(row):
        if val % 2 == 0:
            if i == 0:
                result.append(val * 2)
            else:
                result.append(val)
        elif val % 3 == 0:
            result.append(val + 1)
print(result)