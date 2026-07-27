original = [1, [2, 3], 4, [5, 6]]
copy = original.copy()
copy[1].append(7)
print(original)
print(copy)