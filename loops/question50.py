"create a calorie estimator for popular bengali sweets"

calories = {
    "rasgulla": 140,
    "sandesh": 120,
    "misty doi": 150,
    "chomchom": 160,
    "payesh": 180
}

sweet = input("Enter a Bengali sweet: ").strip().lower()
if sweet in calories:
    print(f"{sweet.title()} has approximately {calories[sweet]} calories.")
elif sweet == "sandesh":
    print("Sandesh has approximately 120 calories.")
    print("Sweet not in the estimator. " \
    "Try rasgulla, sandesh, misty doi, chomchom, or payesh.")
