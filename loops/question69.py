words = ["cat", "dog", "bird", "fish"]
result = []
for word in words:
    if len(word) == 3:
        for i in range(len(word)):
            if word[i] in "aeiou":
                new_word = word[:i] + word[i].upper() + word[i+1:]
                result.append(new_word)
                break
        else:
            result.append(word[::-1])
    elif len(word) == 4:
        if word[0] in "aeiou":
            result.append(word[1:] + word[0])
        else:
            result.append(word)
print(result)