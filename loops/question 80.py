"""
Take 2 numbers (a, b) from user and print all odd numbers from
 a to b inclusive.
"""

# read input numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    a, b = b, a

for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)