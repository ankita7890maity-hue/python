'''
take 10 numbers from the user and store in a list, then print
 the numbers at odd indices
'''
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

for i in range(10):
    if i % 2 != 0:
        print(f"Number at odd index {i}: {numbers[i]}")
        