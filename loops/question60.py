# Guess the output of the following 
items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in reversed(items[2:7]):
    if num % 2 == 0:
        continue
    if num < 4:
        break
    print(num)