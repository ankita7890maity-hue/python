s = "abcdef"
result = ""
for i in range(len(s)):
    if i % 2 == 0:
        for j in range(i, len(s)):
            if s[j] == s[i]:
                result += s[j].upper()
                break
        else:
            result += s[i]
    else:
        continue
print(result)