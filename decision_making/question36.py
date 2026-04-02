'''
Problem: Help negotiate book prices at College Street based on book condition.
- New book: Pay marked price
- Like new: "Ask for 10% discount"
- Good condition: "Ask for 20% discount"
- Fair condition: "Ask for 30% discount"
- Poor condition: "Ask for 50% discount or look elsewhere"
'''

condition = input("Enter book condition (new/like new/good/fair/poor): ").lower()

if condition == "new":
    print("Pay marked price")
elif condition == "like new":
    print("Ask for 10% discount")
elif condition == "good":
    print("Ask for 20% discount")
elif condition == "fair":
    print("Ask for 30% discount")
elif condition == "poor":
    print("Ask for 50% discount or look elsewhere")
else:
    print("Please enter a valid condition")