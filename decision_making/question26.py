'''Take a number (1–7) and print the day name accordingly.
If the user enters 1, print Monday. If the user enters 2 print Tuesday.
 Do this for the numbers 3 to 7 as well. 
 If the user enters a number out of the range, provide an appropriate message of your choice.'''

day = int(input("Enter day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Bhai, 1 se 7 ke beech number daal 😅")
