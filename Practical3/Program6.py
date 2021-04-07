# 6.Write a program to implement method overriding.

class Dog:

    legs = 4
    sound = "bark"

    def speed(self):
        print("Dog has a speed of 40kmph")


class Cat(Dog):

    legs = 4
    sound = "Meow"

    def speed(self):
        print("Cat has a speed of 20kmph")


JohnCat = Cat()
JohnCat.speed()