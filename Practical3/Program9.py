# 9.Write a program to implement abstraction.

from abc import ABC


class Car(ABC):

    # Abstract method
    def speed(self):
        pass


class Honda(Car):

    def speed(self):
        print("Honda has speed of 120kmph")


class Audi(Car):

    def speed(self):
        print("Audi has speed of 240kmph")


class Suzuki(Car):

    def speed(self):
        print("Suzuki has speed of 190kmph")


# Calling methods
HondaCity = Honda()
HondaCity.speed()

AudiA6 = Audi()
AudiA6.speed()

SuzukiNexa = Suzuki()
SuzukiNexa.speed()
