'''
The loop goes through each character in "hello". 
When it encounters 'l', the continue statement skips the print statement. 
So it prints 'h', skips the first 'l', prints 'e', skips the second 'l', and prints 'o'.
'''
word="hello"
for char in word:
    if char =='1':
        continue
    print("char,end=")
    