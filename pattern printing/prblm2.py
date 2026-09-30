a=1
rows=5
for i in range(1, rows+1):
    for j in range(i):
        print(a, end="")
        if a == 1:
            a = 0
        else:
            a = 1
    print()