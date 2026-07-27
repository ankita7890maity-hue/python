# Guess the output of the following code:
s = "abcdefghijk"
window_size = 3
result = []
i = 0
while i <= len(s) - window_size:
    window = s[i:i+window_size]
    if len(set(window)) == window_size:
        vowel_count = sum(1 for c in window if c in "aeiou")
        if vowel_count == 1:
            result.append(window)
    i += 1
print(result)