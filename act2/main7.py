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

print(Student.get_count())