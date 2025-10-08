class Student:

    count = 0
    total_gpa=0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} has a gpa of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total number of students: {cls.count} with the total gpa of {cls.total_gpa}"

    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"

student1 = Student("Mateus", 2.0)
student2 = Student("leo", 3.0)

print(Student.get_count())
print(Student.get_average())