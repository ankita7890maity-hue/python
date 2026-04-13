'''
The loop goes through each item in the list. If the item is "banana",
 it's printed in uppercase. Otherwise, it’s printed as-is.
 '''

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	if fruit == "banana":
		print(fruit.upper())
	else:
		print(fruit)