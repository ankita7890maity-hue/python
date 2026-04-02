'''
Question : Kali Puja Fireworks Permission -
Write a program to check fireworks permission during Kali Puja based on location and time.

Input: Take location (string: "residential" or "commercial") and hour (0-23) as input
Output: Print "Allowed" or "Not Allowed"

Logic:
If residential area:
    If time between 18-22: Allowed
    Else: Not Allowed

If commercial area:
    If time between 16-23: Allowed
    Else: Not Allowed
'''

location = input("Enter location type (residential/commercial): ")
hour = int(input("Enter hour (0-23): "))

if location == "residential":
    if hour >= 18 and hour <= 22:
        permission = "Allowed"
    else:
        permission = "Not Allowed"
else:  # commercial
    if hour >= 16 and hour <= 23:
        permission = "Allowed"
    else:
        permission = "Not Allowed"

print(f"Fireworks: {permission}")