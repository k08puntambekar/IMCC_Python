#  3. Write a program to implement constructor.

class constructorDemo():

    def __init__(self, student_id, student_name, roll):
        self.student_id = student_id
        self.student_name = student_name
        self.roll = roll

    def display(self):
        print("Student ID : ", self.student_id)
        print("Student Name : ", self.student_name)
        print("Student Roll No : ", self.roll)


Student1 = constructorDemo(101, "Kaushik", 37)
Student1.display()
