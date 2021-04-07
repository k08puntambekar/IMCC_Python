# 4. Write a program to implement multiple inheritance.

class Student:

    def __init__(self, student_id, student_name, roll):
        self.student_id = student_id
        self.student_name = student_name
        self.roll = roll

    def display_student(self):
        print("Student ID : ", self.student_id)
        print("Student Name : ", self.student_name)
        print("Student Roll No : ", self.roll)


class Teacher:

    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

    def display_teacher(self):
        print("Teacher ID : ", self.teacher_id)
        print("Teacher Name : ", self.teacher_name)


class College(Student, Teacher):

    def __init__(self, student_id, student_name, roll, teacher_id, teacher_name):
        Student.__init__(student_id, student_name, roll)
        Teacher.__init__(teacher_id, teacher_name)


IMCC = College(101, "Kaushik", 43, 1, "Rahul")
IMCC.display_student()
IMCC.display_teacher()
