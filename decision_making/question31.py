'''
Predict crowd levels at pandal hopping based on time of day.
- 6 AM to 10 AM: "Light crowd - perfect for photography"
- 11 AM to 4 PM: "Moderate crowd - good time to visit"
- 5 PM to 10 PM: "Heavy crowd - expect long queues"
- 11 PM to 5 AM: "Very light crowd - peaceful experience"
'''

hour = int(input("Enter current hour (24-hour format): "))

if 6 <= hour <= 10:
    print("Light crowd - perfect for photography")
elif 11 <= hour <= 16:
    print("Moderate crowd - good time to visit")
elif 17 <= hour <= 22:
    print("Heavy crowd - expect long queues")
elif 23 <= hour <= 24 or 0 <= hour <= 5:
    print("Very light crowd - peaceful experience")
else:
    print("Invalid time entered")