# 5. Write a program to implement polymorphism.

class Honda:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print("Honda car name is : ", self.name, " and color is : ", self.color)


class Audi:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print("Audi car name is : ", self.name, " and color is : ", self.color)


HondaCar = Honda("Honda City", "White")
AudiCar = Audi("A6", "Black")

for car in (HondaCar, AudiCar):
    car.display()

