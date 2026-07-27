'''
question  - Take a positive number from user.
Until the user enters a positive number, keep
asking the user for a number.
Check whether it is a prime number or not.

prime number maane amon number jeta k
khali 1 aar oi number ta nije divide maarte parbe.

'''
while True:
    n = int(input("Enter a positive number: "))
    if n > 0:
        break
    print("Please enter a positive number.")

countdivisors= 0  
for i in range (1,n+1):
    if (n%i==0):
        countdivisors+=1
if(countdivisors==2):
    print("IT's a prime no")
else:
    print("not prime  ")