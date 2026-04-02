'''"Question: Bengali Sweet Shop Discount
A sweet shop offers 10% discount if purchase is above ₹500.
Write a program to ask the user for the purchase amount and then calculate final amount after discount.
Expected Output Format:
Display original amount, discount, and final amount"'''

amount=float(input("enter purchase ammount"))
if amount > 500:
    discount=amount*0.10
    final_amount= discount-amount
    print(f"original_amount:{amount}")
    print(f"original_discount:{discount}")
    print(f"final_amount:{final_amount}")

