'''
Question 5: Write a program to suggest Poila Boishakh celebration venue based on budget and group size.
'''

budget = float(input("Enter budget: "))
group_size = int(input("Enter group size: "))

if budget < 1000:
 if group_size <= 50:
        venue = "home celebration"
    else:
        venue = "small community hall"
elif budget < 1000:
 if group_size <= 20:
        venue = "local restaurant"
    else:
        venue = "banquet hall"
elif budget < 30000:
    venue = "banquet hall"
else:
    venue = "luxury resort"

print(f"Suggested venue for a group of {group_size} with a budget of {budget}: {venue}.")