 # Guess the output of the following code:
letters = ['a', 'b', 'c', 'd', 'e', 'f']
for char in letters:
    if char in letters[2:4]:
        if char == 'd':
            break
        continue
    print(char)
