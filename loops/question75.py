# Guess the output of the following code:
s = "level"
indices = []
for i in range(len(s)):
    if s[i] == s[-(i+1)]:
        indices.append(i)
        
result = ""
for i in indices:
    if i % 2 == 0:
        result += s[i].upper()
    else:
        result += s[i]
        
if not result:
    result = "empty"
    
print(result)