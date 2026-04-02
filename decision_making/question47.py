'''
Question : PVR Cinema Ticket Pricing - 
A PVR cinema charges different prices based on age, show timing, and membership status:

Children (age < 12): ₹150 for matinee, ₹200 for evening/night
Adults (12-59): ₹250 for matinee, ₹350 for evening/night
Senior Citizens (60+): ₹180 for matinee, ₹250 for evening/night
PVR Privilege members get 15% discount on all tickets
Students (age 13-25) get additional ₹50 off if they're not already members

Sample Input: Age = 22, Show = "evening", Member = "no", Student = "yes"
Expected Output: Ticket Price: ₹300
'''

age=int(input("enter your age: "))
showtime=input("enter show timing (matinee/evening/night): ")
member=input("Do you have pvr membership (yes/no): ")
student_status=input("are you student (yes/no): ")
price=0
if showtime == "matinee":
	if age < 12:
		price = 150
	elif 12 <= age < 59:
		price = 250
	else:
		price = 180
if showtime in ["evening", "night"]:
	if age < 12:
		price = 200
	elif 12 <= age < 59:
		price = 350
	else:
		price = 250

if (member == 'y' or member == "yes"):
	discount = 0.15 * price
	price -= discount

if (student_status == "y" and 13 < age <= 25):
	price = price - 50

print(f"your ticket price = {price}")
