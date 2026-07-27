'''
Question 4 : A PVR cinema charges different prices based on age, show timing, and membership status:

Children (age < 12): ₹150 for matinee, ₹200 for evening/night
Adults (12-59): ₹250 for matinee, ₹350 for evening/night
Senior Citizens (60+): ₹180 for matinee, ₹250 for evening/night
PVR Privilege members get 15% discount on all tickets

Sample Input: Age = 22, Show = "evening", Member = "no"
Expected Output: Ticket Price: ₹350
'''

def calculate_ticket_price(age, show, member):
    show = show.strip().lower()
    if age < 12:
        prices = {'matinee': 150, 'evening': 200, 'night': 200}
    elif age < 60:
        prices = {'matinee': 250, 'evening': 350, 'night': 350}
    else:
        prices = {'matinee': 180, 'evening': 250, 'night': 250}

    if show no5tt in prices:
        raise (f"Invalid show timing: {show}")

    member = member.strip().lower()
    price = prices[show]
    if member == 'yes':
        price = round(price * 0.85, 2)

    return price