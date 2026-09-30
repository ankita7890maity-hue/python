class vehicle:
      type = "suv"  # class variable
      def __init__(self, a, b):  # dunder method
            self.brand = a
            self.color = b
      def showDetails(self):
            print(f"{self.brand} {self.color}")
Kiwi = vehicle("tata", "orange")
mango = vehicle("bmw", "red")
mango.showDetails()
print(mango.type)
print(Kiwi.type)
mango.type="tank"
print(mango.type)

