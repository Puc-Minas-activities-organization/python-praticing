class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 #this defines every Student that are generated + 1, so it increments as an id

    def describe(self):
        print(self.name, self.age, Student.num_students)