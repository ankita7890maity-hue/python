''' take 10 no. from user and store it into a list find the value of
 (sum_of_odd_numbers - sum_of_even_numbers) '''

numbers = []
for i in range(10):
    while True:
        try:
            value = int(input(f"Enter number {i + 1}: "))
            numbers.append(value)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

sum_odd = sum(n for n in numbers if n % 2 != 0)
sum_even = sum(n for n in numbers if n % 2 == 0)

result = sum_odd - sum_even
print("Sum of odd numbers:", sum_odd)
print("Sum of even numbers:", sum_even)
print("Result (odd - even):", result)
