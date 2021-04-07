# 7.Write a program to implement composition.

class Company:

    def __init__(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address

    def m1(self):
        print("You are in", self.company_name, "company based in ", self.company_address)


class Employee:

    def __init__(self, company_name, company_address):
        self.obj = Company(company_name, company_address)

    def m2(self):
        print("You are with an employee from this company")
        self.obj.m1()


emp = Employee("Wipro", "Pune")
emp.m2()
