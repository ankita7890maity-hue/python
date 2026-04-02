'''
Question: Voting Eligibility
Write a program that takes a person's age as input and determines if they are eligible to vote in West Bengal elections. If eligible, also check if they are a senior citizen (60+ years) for priority voting.

Expected Output Format:
If age < 18: "Not eligible to vote"
If age 18-59: "Eligible to vote"
If age >= 60: "Eligible to vote with senior citizen priority"
'''

age = int(input("Enter your age: "))

if age < 18:
    print("Not eligible to vote")
else:
    if age >= 60:
        print("Eligible to vote with senior citizen priority")
    else:
        print("Eligible to vote")