# Guess the output of the following code:
x = [1, 2, 3, 4, 5]
i = 0
while i < len(x):
    if x[i] % 2 == 0:
        x.append(x[i] * 2)
        if len(x) > 8:
            break
    i += 1
print(x)