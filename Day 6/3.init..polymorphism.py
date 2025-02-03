class car():
    wheels=4
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print("the brand is: %s" %(self.brand) )  
    def __str__(self):
        return f"Car(Brand: {self.brand}, Wheels: {self.wheels})"

car1=car("toyato")
car2=car("bmw")
print(car1)
print(car2)

car1.display()
car2.display()

car.wheels=6
print(car1.wheels)
print(car2.wheels)
        