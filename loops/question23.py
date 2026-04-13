'''
Even numbers are multiplied by 10, odd numbers are printed as-is.
'''
for num in range(1, 11):
	if num % 2 == 0:
		print(num * 10)
	else:
		print(num)