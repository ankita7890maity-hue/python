'''
Problem: Suggest appropriate clothing for Kolkata weather.
- Temperature > 35°C: "Wear light cotton clothes and carry water"
- Temperature 25-35°C: "Comfortable weather - normal clothes"
- Temperature 15-24°C: "Pleasant weather - light jacket recommended"
- Temperature < 15°C: "Cold weather - wear warm clothes"
'''

temperature = float(input("Enter temperature in Celsius: "))

if temperature > 35:
    print("Wear light cotton clothes and carry water")
elif 25 <= temperature <= 35:
    print("Comfortable weather - normal clothes")
elif 15 <= temperature <= 24:
    print("Pleasant weather - light jacket recommended")
elif temperature < 15:
    print("Cold weather - wear warm clothes")
