'''Create a program that calculates metro fare based on distance traveled.
For distances up to 5 km, fare is ₹10. For distances above 5 km, fare is ₹15.
Expected Output Format:
Display the fare amount with appropriate message."'''


distance=float(input("enter distance in km:"))
if distance <= 5:
	fare = 10
else:
	fare = 15
print(f"Fare: ₹{fare}")