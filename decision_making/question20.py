'''Write a program to take attendance % from user.
If >= 75%, print "Safe zone mein hai tu bhai 😎",
else "Bhai!! tere lagne wale hai exams mein 😥".'''

attendance = float(input("Attendance % daal: "))
if attendance >= 75:
    print("Safe zone mein hai tu bhai 😎")
else:
    print("Bhai!! tere lagne wale hai exams mein 😥")