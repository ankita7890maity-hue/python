 
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in data[2:8]:
    if num % 2 == 0:
        continue
    if num > 7:
        break
    print(num * 2)