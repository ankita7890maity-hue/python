numbers = [1, 2, 3, 4, 5]
operations = ['+', '-', '*', '/', '%']
result = numbers[0]
for i in range(1, len(numbers)):
    op = operations[(i-1) % len(operations)]
    if op == '+':
        result += numbers[i]
    elif op == '-':
        result -= numbers[i]
    elif op == '*':
        result *= numbers[i]
    elif op == '/':
        if numbers[i] != 0:
            result //= numbers[i]
    elif op == '%':
        if numbers[i] != 0:
            result %= numbers[i]
print(int(result))