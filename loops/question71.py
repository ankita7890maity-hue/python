text = "abcdefgh"
pattern = [2, 1, 3, 0]
result = ""
i = 0
while i < len(text):
    step = pattern[i % len(pattern)]
    if step == 0:
        break
    result += text[i]
    i += step
print(result)