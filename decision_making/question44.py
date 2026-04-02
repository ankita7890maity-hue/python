'''
Question: Kolkata Tram Service Status
Write a program to check tram service status based on weather and time.

Input: Take weather (string: "clear", "rain", "storm") and hour (0-23) as input
Output: Print service status
Logic:
If storm: "Service suspended"
Else if rain:
    If hour between 6-22: "Limited service"
    Else: "No service"
Else (clear):
    If hour between 5-23: "Full service"
    Else: "No service"
'''

weather = input("Enter weather (clear/rain/storm): ")
hour = int(input("Enter hour (0-23): "))

if weather == "storm":
    status = "Service suspended"
else:
    if weather == "rain":
        if hour >= 6 and hour <= 22:
            status = "Limited service"
        else:
            status = "No service"
    else:  # clear
        if hour >= 5 and hour <= 23:
            status = "Full service"
        else:
            status = "No service"

print(f"Tram service: {status}")