'''
Only values greater than 7 are appended to list b.
'''
a=[5,10,15]
b=[]
i=0
while i<len(a):
    if a [i] > 7 :
        b.append (a[i])
        i+=1
        print(b)
        