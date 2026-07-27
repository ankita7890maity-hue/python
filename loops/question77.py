text = "Hello World"
result = ""
skip_next = False
for i, char in enumerate(text):
    if skip_next:
        skip_next = False
        continue
    if char.isupper():
        if i + 1 < len(text) and text[i + 1].islower():
            result += char.lower() + text[i + 1].upper()
            skip_next = True
        else:
            result += char
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(result)