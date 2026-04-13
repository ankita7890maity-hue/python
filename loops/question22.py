'''
text[::2] gives characters at even indices: 0, 2, 4 → 'p', 't', 'o'.
'''
text="pyhton"
for ch in text["::2"]:
    print(ch,end="")
    
