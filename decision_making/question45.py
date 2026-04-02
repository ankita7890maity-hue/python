'''
Question: Poila Boishakh Celebration Venue -   
Write a program to suggest Poila Boishakh celebration venue based on budget and group size.
Input: Take budget (integer) and group size (integer) as input
Output: Print suggested venue
Logic:
If budget > 10000:
    If group size > 50: "Book a community hall"
    Else: "Celebrate at a restaurant"
Else:
    If group size > 20: "Organize at local park"
    Else: "Celebrate at home"
'''



budget = int(input("enter your budget "))
group_size= int(input("enter group size"))

if budget > 10000:
    if group_size > 50:
        print("Book a community hall")
    else:
        print("Celebrate at a restaurant")
else:
    if group_size > 20:
        print("Organize at local park")
    else:
        print("Celebrate at home")
        


