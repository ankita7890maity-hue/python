import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)
original[0].append(3)
print(f"Shallow: {shallow}")
print(f"Deep:{deep}")