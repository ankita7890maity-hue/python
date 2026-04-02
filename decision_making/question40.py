'''Question: Darjeeling Tea Grade Classifier
Write a program to classify Darjeeling tea based on price and quality rating.

Input: Take price per kg (float) and quality rating (1-10) as input
Output: Print tea grade: "Premium", "Standard", or "Basic"

Logic:
If price > 1000:
    If quality >= 8: Premium
    Else: Standard

Else:
    If quality >= 6: Standard
    Else: Basic'''
price = float(input("Enter price per kg: "))
quality = int(input("Enter quality rating (1-10): "))

if price > 1000:
    if quality >= 8:
        grade = "Premium"
    else:
        grade = "Standard"
else:
    if quality >= 6:
        grade = "Standard"
    else:
        grade = "Basic"
print(f"Tea grade: {grade}")