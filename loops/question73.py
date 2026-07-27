

data = "12a34b56c78"
digits = []
letters = []
i = 0
while i < len(data):
    if data[i].isdigit():
        j = i
        while j < len(data) and data[j].isdigit():
            j += 1
        digits.append(int(data[i:j]))
        i = j
    elif data[i].isalpha():
        letters.append(data[i])
        i += 1
    else:
        i += 1
        
result = sum(digits) + len(letters)
print(result)