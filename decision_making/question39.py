'''Question: Howrah Bridge Traffic Status - 
Write a program to determine traffic status on Howrah Bridge based on time and vehicle count.

Input: Take hour (0-23) and vehicle count as input.
Output: Print traffic status: "Light", "Moderate", or "Heavy"

Logic:
If hour is between 7-10 or 17-20 (rush hours) -> if vehicles are greater than 500, then traffic status is "Heavy",
 else it is "Moderate"
If it is (non-rush hours) and the vehicles count is greater than 300, then traffic status is "Moderate", else it is "Light"

You can refer this - 
If hour is between 7-10 or 17-20 (rush hours):
    If vehicles > 500: Heavy
    Else: Moderate

Else (non-rush hours):
    If vehicles > 300: Moderate
    Else: Light'''

hour = int(input("Enter hour (0-23): "))
vehicles = int(input("Enter vehicle count: "))

if ((hour >= 7 and hour <= 10) or (hour >= 17 and hour <= 20)):
    if vehicles > 500:
        status = "Heavy"
    else:
        status = "Moderate"
else:
    if vehicles > 300:
        status = "Moderate"
    else:
        status = "Light"

print(f"Traffic status: {status}")