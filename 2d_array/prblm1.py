a=[[5,4,3],[7,8,9],[3,2,1]]
b=[[1,1,1],[0,0,0],[5,4,1]]
c=[]
for i in range(len(a)):
    temp=[]
    for j in range(len(a[i])):
        sum=a[i][j]+b[i][j]
        temp.append(sum)
    c.append(temp)

for i in range (len(c)):
    for j in range(len(c[i])):
        print (c[i][j])




