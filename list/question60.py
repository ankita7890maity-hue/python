original = [1, [2, 3], 4]
copied = original[:]
copied[1].append(5)
copied[0] = 99
print(f"Original: {original}")
print(f"Copied: {copied}")