# call by value
def f1():
    a=10
    b=20
    f2 (a,b)
    print (a,b)

def f2(a,b):
    a=a-20
    b=a
    print(a,b)

f1()

