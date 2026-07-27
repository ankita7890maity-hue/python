'''
Slicing s[i-1:i+1] when i = 1 gives s[0:2] → "py", then i = 3 → s[2:4] → "th".
'''

s="python"
i=1
while i < len(s):
    print(s[i-1:i+1])
    i += 2