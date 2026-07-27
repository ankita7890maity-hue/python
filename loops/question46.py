'''
Explanation: The string "programming" has indices 0-10.
The loop continues when i is even (0, 2, 4, 6, 8, 10),
so it only processes odd indices (1, 3, 5, 7, 9).
These correspond to characters 'r', 'g', 'a', 'm', 'n'.
'''
text="programming"
result=""
for i in range(len(text)):
    if i%2==0:
        continue
    result += text[i]
print(result)