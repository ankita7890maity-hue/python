'''
 List concatenation adds 4 to the list.
   The loop prints all numbers without space or newline due to end="".
   '''
nums = [1, 2, 3]
nums = nums + [4]
for x in nums:
    print(x, end="")