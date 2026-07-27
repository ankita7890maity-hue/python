# Guess the output of the following code:
sentence = "The quick brown fox"
words = sentence.lower().split()
for word in words:
    if len(word) <= 3:
        continue
    for i, char in enumerate(word[::2]):
        if char == 'o':
            break
        print(char, end='')
    print('|', end='')