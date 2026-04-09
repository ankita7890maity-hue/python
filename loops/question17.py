'''
Count the number of digits in a given number.
Example: 1234 → 4 digits
'''

num=1234
count=0
while num > 0:
	num //= 10
	count+=1
	print("number of digits: " ,count)
