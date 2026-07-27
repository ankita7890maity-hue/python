word = "computer"
for i in range(1, len(word), 2):
    if word[i] == 'p':
        break
    print(word[i-1:i+1])