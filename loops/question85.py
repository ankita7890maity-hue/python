
'''
question  - Take a positive number from user.
Until the user enters a positive number, keep
asking the user for a number.
Check whether it is a prime number or not.

prime number maane amon number jeta k
khali 1 aar oi number ta nije divide maarte parbe.

'''
n = int(input("enter a  number: "))
while( n <= 0):
    print("enter a positive number ")
    n = int(input("enter a positive  number: "))
flag = False
if n == 1:
    print("1 is not a prime number.")
else:
    for i in range(2, n):
        if(n % i == 0):
            flag = True
            break
    if flag:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number.")

   
   


