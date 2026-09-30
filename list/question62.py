lst1 = [1, 2, 3]
lst2 = lst1
lst3 = lst1[:]
lst1.append(4)
lst2[0] = 99
print(f"lst1: {lst1}")
print(f"lst2: {lst2}")
print(f"lst3: {lst3}")