# 2. Create a Python class named Rectangle constructed by a length and width and a method
# which will compute the area of a rectangle.

class Rectangle:

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


Rectangle1 = Rectangle(6, 12)
print("Area of Rectangle is : ", Rectangle1.area())
print("Perimeter of Rectangle is : ", Rectangle1.perimeter())
