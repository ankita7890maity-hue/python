class car:
    # brand, color,fuelcapacity
    def __init__(self,a,b,c):
       self.brand=a
       self.color=b
       self.fuelcapacity=c

    def display(self):
        print(f" this is a{self.color}{ self. brand}car")
        print(f"this is a{self. fuelcapacity} liters")

obj1=car("bmw", "black","200")
obj2=car("land rover defender", "plum","80" )

obj1.display()
obj2.display() 
