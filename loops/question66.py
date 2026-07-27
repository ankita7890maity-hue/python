text = "hello world"
vowels = "aeiou"
result = ""
i = 0
while i < len(text):
    if text[i] in vowels:
        for j in range(i+1, len(text)):
            if text[j] not in vowels and text[j] != ' ':
                result += text[j]
                break
        else:
            result += text[i].upper()
    elif text[i] == ' ':
        result += '_'
    i += 1

if __name__ == '__main__':
    print(result)