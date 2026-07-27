'''
print all the prime numbers between 73 and 568
'''

for num in range(73, 569):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
