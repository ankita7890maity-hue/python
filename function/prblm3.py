#behabe like call by reference 
def f1 ():
    a=[5,4,3,2,1]
    b=[10,20,30]
    f2 (a,b)
    print(a,b)

def f2 (a,b):
    a.append(99)
    b.pop()
    print (a,b)

f1()