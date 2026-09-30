data = [1, [2, 3], 4]
backup = data * 2
backup[1].append(99)
print(data)
print(backup)
