# Guess the output of the following code:
words = ["cat", "dog", "bird", "fish"]
for word in words[1:3]:
    if len(word) == 3:
        continue
    for char in word[:2]:
        print(char, end='')
    print()