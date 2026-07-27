''''
The loop goes through indices 0-4. For even numbers (2, 4), 
it doubles them before printing.
So: 1 stays 1, 2 becomes 4, 3 stays 3, 4 becomes 8, 5 stays 5.
'''
numbers=[1,2,3,4,5]
for i in range(len(numbers)):
	if numbers[i] % 2 == 0:
		print(numbers[i]*2)
	else:
		print(numbers[i])
