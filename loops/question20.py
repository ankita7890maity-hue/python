'''
Loop prints each character followed by a dash -, using end="" to print on the same line.
'''
s = "hello "
for i in range(len(s)):
    print(s[i]+"-", end="")