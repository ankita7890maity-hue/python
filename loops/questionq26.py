'''
are replaced with "*", consonants are kept as-is.
'''

word = "amazing"
new = ""
for ch in word:
    if ch in "aeiou":
        new += "*"
    else:
        new += ch
print(new)