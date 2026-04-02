'''Question: Sundarbans Safari Booking - 
Write a program for Sundarbans safari booking based on season and group size.

Input: Take season (string: "winter", "summer", "monsoon") and group size (integer) as input
Output: Print booking status and price per person

Logic:
If season is "monsoon": "Booking closed due to monsoon"
Else:
    If winter and group size > 5: ₹2000 per person
    If winter and group size ≤ 5: ₹2500 per person
    If summer: ₹1500 per person (any group size)'''

season = input("Enter season (winter/summer/monsoon): ")
group_size = int(input("Enter group size: "))

if season == "monsoon":
    print("Booking closed due to monsoon")
else:
    if season == "winter":
        if group_size > 5:
            price = 2000
        else:
            price = 2500
    else:  # summer
        price = 1500
    
    print(f"Booking confirmed! Price: ₹{price} per person")       