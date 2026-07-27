'''
Checks if the number is even or odd using % operator.
'''
a = [1,2,3,4]
i=0
while i<len(a):
    if a[i] %2==0:
        print("even")
    else:
        print("odd")
    i+=1