a = [[5,4,3,2,], [7,8,9,10], [1,2,3,4]]
p = 0
q = 0


for i in range (len(a)):
    for j in range (len(a[i])):
        if j % 2 == 0:
            p += a[i][j]
        else:
            q += a[i][j]

print(p-q)