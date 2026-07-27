data = [[1, 2], [3, 4], [5, 6]]
for i, row in enumerate(data):
    if i == 1:
        continue
    for num in row:
        print(num, end=' ')
    print()