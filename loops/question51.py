# Guess the output of the following code:  # pyright: ignore[reportUndefinedVariable]
sentence = "Python is awesome"
words = sentence.split()
for word in words:
    if word[0] == 'i':
        continue
    print(word[:-1])