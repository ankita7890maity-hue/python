'''
Problem: Create a calorie estimator for popular Bengali sweets.
- Rasgulla: 150 calories
- Sandesh: 120 calories
- Mishti Doi: 180 calories
- Chomchom: 200 calories
- If unknown sweet, show "Calorie information not available"
'''

sweet = input("Enter Bengali sweet name: ").lower()

if sweet == "rasgulla":
    print("Rasgulla contains approximately 150 calories")
elif sweet == "sandesh":
    print("Sandesh contains approximately 120 calories")
elif sweet == "mishti doi":
    print("Mishti Doi contains approximately 180 calories")
elif sweet == "chomchom":
    print("Chomchom contains approximately 200 calories")
else:
    print("Calorie information not available")