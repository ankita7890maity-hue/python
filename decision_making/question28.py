'''Input day and show mess special menu -
if monday, then "nan-puri aar ghoogni 😋"
if tuesday, then "matar paneer aar naan 🥘"
if wednesday, then, "bhetki maach er paturi 😍"
if thursday, then, "shahi paneer aar aalo-ka-paratha 🍛"
if friday, then, "chicken egg rolls 😎"
if saturday, then, "aaloo-posto aar luchi 😋 "
if sunday, then, "chicken biriyani 🔥"'''

day = input("Enter day: ").lower()
if day == "monday":
    print("nan-puri aar ghoogni 😋")
elif day == "tuesday":
    print("matar paneer aar naan 🥘")
elif day == "wednesday":
    print("bhetki maach er paturi 😍")
elif day == "thursday":
    print("shahi paneer aar aalo-ka-paratha 🍛")
elif day == "friday":
    print("chicken egg rolls 😎")
elif day == "saturday":
    print("aaloo-posto aar luchi 😋 ")
elif day == "sunday":
    print("chicken biriyani 🔥")
else:
    print("Bhai, ye din to mess mein close lag raha hai 😅")