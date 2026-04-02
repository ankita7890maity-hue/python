'''Write a program to take message status (seen/delivered) from user.
If seen, print "Ab wait kar result ka 😶",
else "Dekhaa! maine bola tha, woh tujhe ghaas nahi dalegi 🤣".'''

status = input("Crush ne message dekha? (seen/delivered): ")
if status.lower() == "seen":
    print("Ab wait kar result ka 😶")
else:
    print("Dekhaa! maine bola tha, woh tujhe ghaas nahi dalegi 🤣")