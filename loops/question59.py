# Guess the output of the following code:
text = "hello world"
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(text)):
    if text[i] in vowels:
        continue
    if i > 6:
        break
    print(text[i], end='')