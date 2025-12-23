#Write a Python program to implement Inheritance by creating a Parent Class Vehicle 
# with a constructor that has details like name, maximum speed, and mileage. 
# Then, create a Child Class Bus that inherits Class Vehicle. 
# Finally, showcase Inheritance to display the details of the Vehicle Bus named - 
# School Volvo.
class Vehicle:
    def __init__(self,name,maximum_speed,mileage):
        self.name=name
        self.maximum_speed=maximum_speed
        self.mileage=mileage
    def display(self):
        print(self.name)
        print(self.maximum_speed)
        print(self.mileage)

class Bus(Vehicle):
    pass
v=Bus("Volvo","75","15")
v.display()