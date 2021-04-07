# 10. Write a program to implement to show the use of access specifier.

class Parent:

    # public
    var1 = None

    # protected
    _var2 = None

    # private
    __var3 = None

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def display_public(self):
        print("This is a public member")

    def display_protected(self):
        print("This is a protected member")

    def display_private(self):
        print("This is a private member")


class Child(Parent):

    def __init__(self, var1, var2, var3):
        super(Child, self).__init__(var1, var2, var3)

    def print_protected(self):
        self.display_protected()


childObj = Child("Hello", "every", "one")

childObj.display_public()
childObj.display_protected()
childObj.display_private()